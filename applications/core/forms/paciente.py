from django import forms
from django.forms import ModelForm
from applications.core.models import Paciente

class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = ["nombres", "apellidos", "fecha_nacimiento", "tipo_sangre"]

        widgets = {
            "nombres": forms.TextInput(attrs={
                "placeholder": "Ingrese nombres del paciente",
                "id": "id_nombres",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 "
                         "focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 "
                         "dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 "
                         "dark:focus:border-blue-500 dark:shadow-sm-light",
            }),
            "apellidos": forms.TextInput(attrs={
                "placeholder": "Ingrese apellidos del paciente",
                "id": "id_apellidos",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 "
                         "focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 "
                         "dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 "
                         "dark:focus:border-blue-500 dark:shadow-sm-light",
            }),
            "fecha_nacimiento": forms.DateInput(attrs={
                "type": "date",
                "id": "id_fecha_nacimiento",
                "class": "form-control",
            }),
            "tipo_sangre": forms.Select(attrs={
                "id": "id_tipo_sangre",
                "class": "form-control"
            }),
        }

        labels = {
            "nombres": "Nombres del Paciente",
            "apellidos": "Apellidos",
            "fecha_nacimiento": "Fecha de Nacimiento",
            "tipo_sangre": "Tipo de Sangre",
        }

    def clean_nombres(self):
        return self.cleaned_data.get("nombres").title()

    def clean_apellidos(self):
        return self.cleaned_data.get("apellidos").title()
