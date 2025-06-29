from django import forms
from django.forms import ModelForm
from applications.core.models import TipoGasto

class TipoGastoForm(ModelForm):
    class Meta:
        model = TipoGasto
        fields = ["nombre", "descripcion", "activo"]

        labels = {
            "nombre": "Nombre del Tipo de Gasto",
            "descripcion": "Descripción del Gasto",
            "activo": "¿Activo?",
        }

        widgets = {
            "nombre": forms.TextInput(attrs={
                "placeholder": "Ingrese nombre del tipo de gasto",
                "id": "id_nombre",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg "
                         "focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 "
                         "dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 "
                         "dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }),
            "descripcion": forms.Textarea(attrs={
                "placeholder": "Ingrese una descripción (opcional)",
                "id": "id_descripcion",
                "rows": 3,
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg "
                         "focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 "
                         "dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 "
                         "dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }),
            "activo": forms.CheckboxInput(attrs={
                "class": "h-5 w-5 text-blue-600 focus:ring-blue-500 border-gray-300 rounded "
                         "dark:bg-gray-700 dark:border-gray-600",
            }),
        }

        error_messages = {
            "nombre": {
                "unique": "Ya existe un tipo de gasto con este nombre.",
                "required": "El nombre es obligatorio.",
            },
        }

    def clean_nombre(self):
        return self.cleaned_data.get("nombre").upper()
