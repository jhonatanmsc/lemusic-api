from django.shortcuts import render
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from apps.localidade.models import Cidade, Bairro, Endereco
from apps.localidade.serializers import CidadeSerializer, BairroSerializer, EnderecoSerializer


class CidadeViewSet(ModelViewSet):
    name = 'cidade-api'
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer
    permission_classes = (IsAdminUser,)


class BairroViewSet(ModelViewSet):
    name = 'bairro-api'
    queryset = Bairro.objects.all()
    serializer_class = BairroSerializer
    permission_classes = (IsAdminUser,)


class EnderecoViewSet(ModelViewSet):
    name = 'endereco-api'
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
    permission_classes = (IsAdminUser,)
