from django import forms
from django.forms import ModelForm
from applications.core.models import FotoPaciente

class FotoPacienteForm(ModelForm):
    class Meta:
        model = FotoPaciente
        fields = ["paciente", "imagen", "descripcion"]

        widgets = {
            "paciente": forms.Select(attrs={
                "id": "id_paciente",
                "class": "form-control",
            }),
            "imagen": forms.ClearableFileInput(attrs={
                "id": "id_imagen",
                "class": "form-control-file",
            }),
            "descripcion": forms.Textarea(attrs={
                "placeholder": "Ingrese una descripción (opcional)",
                "id": "id_descripcion",
                "class": "form-control",
                "rows": 3,
            }),
        }

        labels = {
            "paciente": "Paciente",
            "imagen": "Imagen",
            "descripcion": "Descripción",
        }

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get("descripcion")
        return descripcion.capitalize() if descripcion else ""
