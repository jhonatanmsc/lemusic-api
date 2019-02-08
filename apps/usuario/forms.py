from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import Group

from apps.usuario.models import Usuario


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme a senha', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = '__all__'
        exclude = ('password', 'is_staff', 'is_admin', 'is_active', 'user_permissions', 'is_superuser')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active = True
        user.is_staff = True

        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    password = ReadOnlyPasswordHashField(label="Password",
                                         help_text=("As senhas não são registradas no banco de dados, "
                                                    "para alterar sua senha click no link "
                                                    "<a href=\"/admin/password_change/\">alterar senha</a>."))

    class Meta:
        model = Usuario
        fields = '__all__'
        exclude = ('password', 'is_staff', 'is_admin', 'is_active', 'user_permissions', 'is_superuser')
