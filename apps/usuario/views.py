import datetime
import pdb

import jwt
from django.conf import settings
from django.contrib.auth.models import Group, Permission, User
from django.shortcuts import render
from rest_framework import parsers, renderers, status
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.throttling import ScopedRateThrottle
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from apps.usuario.models import Usuario
from apps.usuario.serializers import UsuarioSerializer, GroupSerializer, PermissionSerializer


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
                    'username': user.email,
                    'iat': datetime.datetime.utcnow(),
                    'nbf': datetime.datetime.utcnow() + datetime.timedelta(minutes=-5),
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7)
                }, settings.SECRET_KEY)
                return Response({'token': token})
            except User.DoesNotExist:
                pass
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
