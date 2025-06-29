from django import forms
from applications.doctor.models import DetalleAtencion


class DetalleAtencionForm(forms.ModelForm):
    class Meta:
        model = DetalleAtencion
        fields = '__all__'
        labels = {
            'atencion': 'Atención Médica',
            'medicamento': 'Medicamento',
            'cantidad': 'Cantidad',
            'prescripcion': 'Prescripción',
            'duracion_tratamiento': 'Duración del Tratamiento (días)',
            'frecuencia_diaria': 'Frecuencia Diaria (veces por día)',
        }
        widgets = {
            'atencion': forms.Select(attrs={
                'class': 'form-control rounded-full text-center'
            }),
            'medicamento': forms.Select(attrs={
                'class': 'form-control rounded-full text-center'
            }),
            'cantidad': forms.NumberInput(attrs={
                'class': 'form-control rounded-full text-center',
                'placeholder': 'Ejemplo: 2'
            }),
            'prescripcion': forms.Textarea(attrs={
                'class': 'form-control rounded-2xl text-center',
                'placeholder': 'Ejemplo: Tomar una pastilla después de cada comida',
                'rows': 3,
            }),
            'duracion_tratamiento': forms.NumberInput(attrs={
                'class': 'form-control rounded-full text-center',
                'placeholder': 'Ejemplo: 7',
            }),
            'frecuencia_diaria': forms.NumberInput(attrs={
                'class': 'form-control rounded-full text-center',
                'placeholder': 'Ejemplo: 3',
            }),
        }

    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')
        if cantidad < 1:
            raise forms.ValidationError("La cantidad debe ser al menos 1.")
        return cantidad

    def clean_prescripcion(self):
        texto = self.cleaned_data.get('prescripcion', '').strip()
        if not texto:
            raise forms.ValidationError("La prescripción no puede estar vacía.")
        return texto
