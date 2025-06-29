import re
from django import forms
from django.forms import ModelForm
from django.contrib.auth.hashers import make_password

from applications.security.models import User, Group
from django.contrib.auth.hashers import make_password


class UserForm(ModelForm):
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            "placeholder": "Ingrese una contraseña segura",
            "id": "id_password",
            'autocomplete': 'new-password',
            "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
        }),
        required=False,
    )

    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput(attrs={
            "placeholder": "Confirme la contraseña",
            "id": "id_password2",  
            'autocomplete': 'new-password',
            "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
        }),
        required=False
    )
    
    
    grupo = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        required=True,
        label="Rol de usuario",
        widget=forms.Select(attrs={
            "class": "form-control",
        })
    )





    class Meta:
        model = User
        fields = [
            "first_name", "last_name", "username", "email", "password",
            "dni", "phone", "direction", "image", "grupo"
        ]
        labels = {
            "first_name": "Nombres",
            "last_name": "Apellidos",
            "username": "Nombre de usuario",
            "email": "Correo electrónico",
            "dni": "Cédula o RUC",
            "phone": "Teléfono",
            "direction": "Dirección",
            "image": "Foto de perfil",
        }
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese nombres"}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese apellidos"}),
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese nombre de usuario"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Ingrese correo electrónico"}),
            "dni": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese cédula o RUC"}),
            "phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese teléfono"}),
            "direction": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese dirección"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }
        error_messages = {
            "email": {
                "unique": "Ya existe un usuario con este correo.",
            },
            "username": {
                "unique": "Ya existe un usuario con este nombre de usuario.",
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('user_permissions', None)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        return email.lower()
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password or password2:
            if password != password2:
                raise forms.ValidationError("Las contraseñas no coinciden.")
            if len(password) < 8:
                raise forms.ValidationError("La contraseña debe tener al menos 8 caracteres.")
        else:
            # Si estamos editando y no hay nueva contraseña, mantener la anterior
            if self.instance.pk:
                cleaned_data["password"] = self.instance.password

        if not self.instance.pk and not password:
            raise forms.ValidationError("Debe ingresar una contraseña para el nuevo usuario.")

        self.cleaned_data.pop("password2", None)
    
    
    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get("password")

        if password:
            if not password.startswith('pbkdf2_'):
                user.password = make_password(password)
            else:
                user.password = password

        if commit:
            user.save()
            grupo = self.cleaned_data.get('grupo')
            if grupo:
                user.groups.set([grupo])  # asigna el grupo (reemplaza grupos previos)
        return user
