import re
from django import forms
from django.forms import ModelForm

from applications.security.models import User, Module

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
            "is_active",
            "is_staff",
            "is_superuser",
        ]
        error_messages = {
            "username": {
                "unique": "Ya existe un usuario con este nombre de usuario.",
            },
            "email": {
                "unique": "Ya existe un usuario con este correo electrónico.",
            },
            "password": {
                "required": "La contraseña es obligatoria.",
                "min_length": "La contraseña debe tener al menos 8 caracteres.",
            },
        }

        widgets = {
            "username": forms.TextInput(attrs={
                "placeholder": "Ingrese nombre de usuario",
                "class": "form-control"
            }),
            "email": forms.EmailInput(attrs={
                "placeholder": "Ingrese correo electrónico",
                "class": "form-control"
            }),
            "first_name": forms.TextInput(attrs={
                "placeholder": "Ingrese nombre",
                "class": "form-control"
            }),
            "last_name": forms.TextInput(attrs={
                "placeholder": "Ingrese apellido",
                "class": "form-control"
            }),
            "password": forms.PasswordInput(attrs={
                "placeholder": "Ingrese contraseña",
                "class": "form-control"
            }),
        }
        labels = {
            "username": "Nombre de Usuario",
            "email": "Correo Electrónico",
            "first_name": "Nombre",
            "last_name": "Apellido",
            "password": "Contraseña",
        }
    def clean_username(self):
        username = self.cleaned_data.get("username")
        if not re.match(r'^[a-zA-Z0-9_]+$', username):
            raise forms.ValidationError("El nombre de usuario solo puede contener letras, números y guiones bajos.")
        return username
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            raise forms.ValidationError("Ingrese un correo electrónico válido.")
        return email
    def clean_password(self):
        password = self.cleaned_data.get("password")
        if len(password) < 8:
            raise forms.ValidationError("La contraseña debe tener al menos 8 caracteres.")
        return password
