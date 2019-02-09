from django.contrib.auth.models import Group, Permission
from rest_framework import serializers

from apps.usuario.models import Usuario


class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        exclude = ('password', 'is_staff', 'is_admin', 'is_active', 'user_permissions', 'is_superuser')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class PermissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Permission
        exclude = ('content_type',)
