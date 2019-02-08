from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser

from apps.localidade.models import Cidade, Bairro
from apps.localidade.serializers import CidadeSerializer, BairroSerializer


class CidadeAPIList(ListAPIView):
    name = 'cidade-api'
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer
    permission_classes = (IsAdminUser,)


class BairroAPIList(ListAPIView):
    name = 'bairro-api'
    queryset = Bairro.objects.all()
    serializer_class = BairroSerializer
    permission_classes = (IsAdminUser,)
