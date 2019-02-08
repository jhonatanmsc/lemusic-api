from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.usuario.forms import UserCreationForm, UserChangeForm
from apps.usuario.models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(ModelAdmin):
    model = Usuario
    change_form = UserChangeForm
    add_form = UserCreationForm

    def get_form(self, request, obj=None, **kwargs):
        if not obj:
            self.form = self.add_form
        else:
            self.form = self.change_form

        return super(UsuarioAdmin, self).get_form(request, obj, **kwargs)
