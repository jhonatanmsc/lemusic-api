from django.contrib import admin

from apps.localidade.models import *

admin.site.register(Cidade)
admin.site.register(Bairro)
admin.site.register(Endereco)
