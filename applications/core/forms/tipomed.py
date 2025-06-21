from django import forms
from django.forms import ModelForm
from applications.core.models import TipoMedicamento

class TipoMedicamentoForm(ModelForm):
    class Meta:
        model = TipoMedicamento
        fields = ["nombre"]

        error_messages = {
            "nombre": {
                "unique": "Ya existe un tipo de medicamento con este nombre.",
                "required": "El nombre es obligatorio.",
            },
        }

        widgets = {
            "nombre": forms.TextInput(attrs={
                "placeholder": "Ingrese nombre del tipo de medicamento",
                "id": "id_nombre",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg "
                         "focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 "
                         "dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 "
                         "dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }),
        }

        labels = {
            "nombre": "Nombre del Tipo de Medicamento",
        }

    def clean_nombre(self):
        return self.cleaned_data.get("nombre").upper()
