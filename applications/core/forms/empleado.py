from django import forms
from django.forms import ModelForm
from applications.core.models import Empleado

class EmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        fields = [
            "nombres", "apellidos", "cedula_ecuatoriana", "dni",
            "fecha_nacimiento", "cargo", "sueldo", "fecha_ingreso",
            "direccion", "latitud", "longitud", "foto"
        ]

        labels = {
            "nombres": "Nombres",
            "apellidos": "Apellidos",
            "cedula_ecuatoriana": "Cédula",
            "dni": "DNI Internacional",
            "fecha_nacimiento": "Fecha de Nacimiento",
            "cargo": "Cargo",
            "sueldo": "Sueldo",
            "fecha_ingreso": "Fecha de Ingreso",
            "direccion": "Dirección",
            "latitud": "Latitud",
            "longitud": "Longitud",
            "foto": "Foto del Empleado",
        }

        error_messages = {
            "cedula_ecuatoriana": {
                "required": "La cédula es obligatoria.",
                "max_length": "La cédula debe tener máximo 10 dígitos.",
            },
            "dni": {
                "max_length": "Máximo 30 caracteres para el DNI.",
            },
            "sueldo": {
                "required": "Debe ingresar el sueldo.",
            },
        }

        widgets = {
            "nombres": forms.TextInput(attrs={
                "placeholder": "Ingrese nombres del empleado",
                "class": "input-text",
            }),
            "apellidos": forms.TextInput(attrs={
                "placeholder": "Ingrese apellidos del empleado",
                "class": "input-text",
            }),
            "cedula_ecuatoriana": forms.TextInput(attrs={
                "placeholder": "Ingrese número de cédula",
                "class": "input-text",
            }),
            "dni": forms.TextInput(attrs={
                "placeholder": "Ingrese pasaporte o documento internacional",
                "class": "input-text",
            }),
            "fecha_nacimiento": forms.DateInput(attrs={
                "type": "date",
                "class": "input-text",
            }),
            "cargo": forms.Select(attrs={
                "class": "input-text",
            }),
            "sueldo": forms.NumberInput(attrs={
                "placeholder": "Ingrese sueldo",
                "class": "input-text",
                "step": "0.01",
            }),
            "fecha_ingreso": forms.DateInput(attrs={
                "type": "date",
                "class": "input-text",
            }),
            "direccion": forms.TextInput(attrs={
                "placeholder": "Ingrese dirección",
                "class": "input-text",
            }),
            "latitud": forms.NumberInput(attrs={
                "placeholder": "Latitud geográfica",
                "class": "input-text",
                "step": "any",
            }),
            "longitud": forms.NumberInput(attrs={
                "placeholder": "Longitud geográfica",
                "class": "input-text",
                "step": "any",
            }),
            "foto": forms.ClearableFileInput(attrs={
                "class": "input-text",
            }),
        }

    def clean_nombres(self):
        return self.cleaned_data.get("nombres", "").strip().title()

    def clean_apellidos(self):
        return self.cleaned_data.get("apellidos", "").strip().title()
    
    
    def clean_cedula_ecuatoriana(self):
        cedula = self.cleaned_data.get("cedula_ecuatoriana", "")
        return str(cedula).strip()

