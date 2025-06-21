from django import forms
from django.forms import ModelForm
from applications.core.models import Diagnostico

class DiagnosticoForm(ModelForm):
    class Meta:
        model = Diagnostico
        fields = ["paciente", "doctor", "descripcion"]

        widgets = {
            "paciente": forms.Select(attrs={
                "id": "id_paciente",
                "class": "form-control",
            }),
            "doctor": forms.Select(attrs={
                "id": "id_doctor",
                "class": "form-control",
            }),
            "descripcion": forms.Textarea(attrs={
                "placeholder": "Ingrese descripción del diagnóstico",
                "id": "id_descripcion",
                "class": "form-control",
                "rows": 4,
            }),
        }

        labels = {
            "paciente": "Paciente",
            "doctor": "Doctor",
            "descripcion": "Descripción del Diagnóstico",
        }

    def clean_descripcion(self):
        return self.cleaned_data.get("descripcion").capitalize()
