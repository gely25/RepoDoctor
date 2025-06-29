from django import forms
from django.forms import ModelForm
from applications.core.models import MarcaMedicamento

class MarcaMedicamentoForm(ModelForm):
    class Meta:
        model = MarcaMedicamento
        fields = ["nombre", "descripcion"]

        labels = {
            "nombre": "Nombre de la Marca",
            "descripcion": "Descripción (opcional)",
        }

        help_texts = {
            "nombre": "Ejemplo: Pfizer, Bayer, Novartis",
            "descripcion": "Descripción general u observaciones sobre esta marca.",
        }

        error_messages = {
            "nombre": {
                "unique": "Ya existe una marca de medicamento con este nombre.",
                "required": "El nombre de la marca es obligatorio.",
            },
        }

        widgets = {
            "nombre": forms.TextInput(attrs={
                "placeholder": "Ingrese el nombre de la marca",
                "id": "id_nombre",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg "
                         "focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 "
                         "dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 "
                         "dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }),
            "descripcion": forms.Textarea(attrs={
                "placeholder": "Ingrese una descripción opcional...",
                "rows": 3,
                "id": "id_descripcion",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg "
                         "focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 "
                         "dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 "
                         "dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }),
        }

    def clean_nombre(self):
        return self.cleaned_data.get("nombre").upper()
