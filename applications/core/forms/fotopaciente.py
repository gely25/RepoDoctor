from django import forms
from applications.core.models import FotoPaciente

class FotoPacienteForm(forms.ModelForm):
    class Meta:
        model = FotoPaciente
        fields = ['paciente', 'imagen', 'descripcion']
        labels = {
            'paciente': 'Paciente',
            'imagen': 'Imagen del Paciente',
            'descripcion': 'Descripción',
        }
        widgets = {
            'paciente': forms.Select(
                attrs={
                    'class': 'form-control rounded-md dark:bg-gray-800 dark:text-white',
                }
            ),
            'imagen': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control-file mt-2 dark:bg-gray-800 dark:text-white',
                    'accept': 'image/*',
                }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control rounded-md dark:bg-gray-800 dark:text-white',
                    'rows': 3,
                    'placeholder': 'Descripción opcional de la imagen...',
                }
            ),
        }
        error_messages = {
            'paciente': {
                'required': 'Debe seleccionar un paciente.',
            },
            'imagen': {
                'required': 'Debe subir una imagen.',
                'invalid': 'El archivo subido no es una imagen válida.',
            },
        }

    def clean_imagen(self):
        imagen = self.cleaned_data.get('imagen')
        if imagen:
            if imagen.size > 5 * 1024 * 1024:
                raise forms.ValidationError("La imagen no debe superar los 5MB.")
            if not imagen.content_type.startswith("image/"):
                raise forms.ValidationError("El archivo debe ser una imagen válida.")
        return imagen
