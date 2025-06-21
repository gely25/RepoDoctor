from django import forms
from django.forms import ModelForm
from applications.core.models import GastoMensual

class GastoMensualForm(ModelForm):
    class Meta:
        model = GastoMensual
        fields = ["tipo", "descripcion", "monto", "fecha"]

        widgets = {
            "tipo": forms.Select(attrs={
                "id": "id_tipo",
                "class": "form-control",
            }),
            "descripcion": forms.Textarea(attrs={
                "placeholder": "Ingrese descripción del gasto",
                "id": "id_descripcion",
                "class": "form-control",
                "rows": 3,
            }),
            "monto": forms.NumberInput(attrs={
                "placeholder": "Ingrese el monto",
                "id": "id_monto",
                "class": "form-control",
            }),
            "fecha": forms.DateInput(attrs={
                "type": "date",
                "id": "id_fecha",
                "class": "form-control",
            }),
        }

        labels = {
            "tipo": "Tipo de Gasto",
            "descripcion": "Descripción",
            "monto": "Monto",
            "fecha": "Fecha",
        }

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get("descripcion")
        return descripcion.capitalize() if descripcion else ""
