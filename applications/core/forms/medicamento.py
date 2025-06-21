from django import forms
from django.forms import ModelForm
from applications.core.models import Medicamento

class MedicamentoForm(ModelForm):
    class Meta:
        model = Medicamento
        fields = ["nombre", "marca", "tipo", "descripcion", "stock"]

        widgets = {
            "nombre": forms.TextInput(attrs={
                "placeholder": "Ingrese nombre del medicamento",
                "id": "id_nombre",
                "class": "form-control",
            }),
            "marca": forms.Select(attrs={
                "id": "id_marca",
                "class": "form-control",
            }),
            "tipo": forms.Select(attrs={
                "id": "id_tipo",
                "class": "form-control",
            }),
            "descripcion": forms.Textarea(attrs={
                "placeholder": "Descripción (opcional)",
                "id": "id_descripcion",
                "class": "form-control",
                "rows": 3,
            }),
            "stock": forms.NumberInput(attrs={
                "placeholder": "Ingrese cantidad disponible",
                "id": "id_stock",
                "class": "form-control",
            }),
        }

        labels = {
            "nombre": "Nombre del Medicamento",
            "marca": "Marca",
            "tipo": "Tipo",
            "descripcion": "Descripción",
            "stock": "Stock Disponible",
        }

    def clean_nombre(self):
        return self.cleaned_data.get("nombre").upper()
