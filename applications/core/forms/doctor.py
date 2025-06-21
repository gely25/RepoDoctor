from django import forms
from django.forms import ModelForm
from applications.core.models import Doctor

class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = ["nombres", "apellidos", "especialidad", "cargo"]

        widgets = {
            "nombres": forms.TextInput(attrs={
                "placeholder": "Ingrese nombres del doctor",
                "id": "id_nombres",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 "
                         "focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 "
                         "dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 "
                         "dark:focus:border-blue-500 dark:shadow-sm-light",
            }),
            "apellidos": forms.TextInput(attrs={
                "placeholder": "Ingrese apellidos del doctor",
                "id": "id_apellidos",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 "
                         "focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 "
                         "dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 "
                         "dark:focus:border-blue-500 dark:shadow-sm-light",
            }),
            "especialidad": forms.Select(attrs={"id": "id_especialidad", "class": "form-control"}),
            "cargo": forms.Select(attrs={"id": "id_cargo", "class": "form-control"}),
        }

        labels = {
            "nombres": "Nombres del Doctor",
            "apellidos": "Apellidos",
            "especialidad": "Especialidad Médica",
            "cargo": "Cargo (opcional)",
        }

    def clean_nombres(self):
        return self.cleaned_data.get("nombres").title()

    def clean_apellidos(self):
        return self.cleaned_data.get("apellidos").title()
