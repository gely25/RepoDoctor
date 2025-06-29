from django import forms
from applications.doctor.models import ServiciosAdicionales

class ServiciosAdicionalesForm(forms.ModelForm):
    class Meta:
        model = ServiciosAdicionales
        fields = '__all__'
        labels = {
            'nombre_servicio': 'Nombre del Servicio',
            'costo_servicio': 'Costo del Servicio',
            'descripcion': 'Descripción',
            'activo': '¿Está Activo?',
        }
        widgets = {
            'nombre_servicio': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ejemplo: Radiografía',
                'autocomplete': 'off'
            }),
            'costo_servicio': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ejemplo: 25.00',
                'step': '0.01',
                'min': '0'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Ejemplo: Examen de sangre de rutina.'
            }),
            'activo': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
        error_messages = {
            'nombre_servicio': {
                'required': 'Este campo es obligatorio.',
                'max_length': 'El nombre del servicio no puede exceder los 255 caracteres.',
            },
            'costo_servicio': {
                'required': 'Este campo es obligatorio.',
                'invalid': 'Ingresa un valor numérico válido.',
            },
            'descripcion': {
                'max_length': 'La descripción es demasiado larga.',
            },
        }

    def clean_costo_servicio(self):
        costo = self.cleaned_data.get('costo_servicio')
        if costo is not None and costo < 0:
            raise forms.ValidationError("El costo no puede ser negativo.")
        return costo
