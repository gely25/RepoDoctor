from django import forms
from django.forms import ModelForm
from applications.core.models import Cargo

class CargoForm(ModelForm):
    class Meta:
        model = Cargo
        fields = ["nombre", "descripcion"]

        error_messages = {
            "nombre": {
                "unique": "Ya existe un cargo con este nombre.",
                "required": "El nombre del cargo es obligatorio.",
            },
        }

        widgets = {
            "nombre": forms.TextInput(attrs={
                "placeholder": "Ingrese nombre del cargo",
                "id": "id_nombre",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg "
                         "focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 "
                         "dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 "
                         "dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }),
            "descripcion": forms.Textarea(attrs={
                "placeholder": "Ingrese una descripción (opcional)",
                "id": "id_descripcion",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg "
                         "focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 "
                         "dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 "
                         "dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                "rows": 3,
            }),
        }

        labels = {
            "nombre": "Nombre del Cargo",
            "descripcion": "Descripción",
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        return nombre.upper()
