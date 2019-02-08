from rest_framework import serializers

from apps.localidade.models import *


class CidadeSerializer(serializers.Serializer):
    class Meta:
        model = Cidade
        fields = '__all__'


class BairroSerializer(serializers.Serializer):
    class Meta:
        model = Bairro
        fields = '__all__'


class EnderecoSerializer(serializers.Serializer):
    class Meta:
        model = Endereco
        fields = '__all__'
