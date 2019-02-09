from django.contrib.auth.models import Group, Permission
from django.shortcuts import render
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from apps.usuario.models import Usuario
from apps.usuario.serializers import UsuarioSerializer, GroupSerializer, PermissionSerializer


class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = (IsAdminUser,)


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAdminUser,)


class PermissionViewSet(ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = (IsAdminUser,)
