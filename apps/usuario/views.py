import datetime
import pdb

import jwt
from django.conf import settings
from django.contrib.auth.models import Group, Permission, User
from django.http import HttpResponse
from rest_framework import parsers, renderers, status, exceptions
from rest_framework.authentication import BaseAuthentication, get_authorization_header, TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from apps.usuario.models import Usuario
from apps.usuario.serializers import UsuarioSerializer, GroupSerializer, PermissionSerializer
from details.settings import PYJWT


class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = (IsAdminUser, IsAuthenticated,)


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAdminUser,)


class PermissionViewSet(ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = (IsAdminUser,)


class ObtainToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # pdb.set_trace()
            try:
                user = Usuario.objects.get(email=request.data['username'])
                token = jwt.encode({
                    'user_id': user.id,
                    'email': user.email,
                    'iat': datetime.datetime.utcnow(),
                    'nbf': datetime.datetime.utcnow() + datetime.timedelta(minutes=-5),
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7)
                }, settings.SECRET_KEY)
                return Response({'token': token})
            except User.DoesNotExist:
                return Response({'error': 'Usuário não existe.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CheckToken(APIView):
    throttle_classes = ()
    permission_classes = ()

    def post(self, request):
        token = jwt.decode(request.data['token'], settings.SECRET_KEY)
        data_exp = datetime.datetime.fromtimestamp(token['exp'])
        if data_exp > datetime.datetime.utcnow():
            diff = data_exp - datetime.datetime.utcnow()
            status_token = {
                'status': 'Token OK.',
                'days_to_expire': diff.days
            }
        else:
            status_token = {
                'status': 'Token Expired.',
                'days_to_expire': -1
            }
        return Response(status_token)


class RefreshToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    def post(self, request):
        token = jwt.decode(request.data['token'], settings.SECRET_KEY)
        diff = datetime.datetime.fromtimestamp(token['exp']) - datetime.datetime.utcnow()
        if diff.days == 0:
            user = Usuario.objects.get(id=token['user_id'])
            serializer = self.serializer_class(data={'username': token['email'], 'password': request.data['password']})
            if serializer.is_valid():
                try:
                    user = Usuario.objects.get(id=token['user_id'])
                    token = jwt.encode({
                        'user_id': user.id,
                        'email': user.email,
                        'iat': datetime.datetime.utcnow(),
                        'nbf': datetime.datetime.utcnow() + datetime.timedelta(minutes=-5),
                        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7)
                    }, settings.SECRET_KEY)
                    return Response({'token': token})
                except User.DoesNotExist:
                    return Response({'error': 'Usuário não existe.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Refresh somente no ultimo dia de validade'}, status=status.HTTP_400_BAD_REQUEST)
