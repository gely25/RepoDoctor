from django import forms
from applications.doctor.models import CitaMedica
from django.core.exceptions import ValidationError
from datetime import date

class CitaMedicaForm(forms.ModelForm):
    class Meta:
        model = CitaMedica
        fields = ['paciente', 'fecha', 'hora_cita', 'estado', 'observaciones']
        labels = {
            'paciente': 'Paciente',
            'fecha': 'Fecha de la Cita',
            'hora_cita': 'Hora de la Cita',
            'estado': 'Estado de la Cita',
            'observaciones': 'Observaciones',
        }
        error_messages = {
            'paciente': {
                'required': 'Debe seleccionar un paciente.',
            },
            'fecha': {
                'required': 'La fecha de la cita es obligatoria.',
                'invalid': 'Ingrese una fecha válida.',
            },
            'hora_cita': {
                'required': 'La hora de la cita es obligatoria.',
                'invalid': 'Ingrese una hora válida.',
            },
            'estado': {
                'required': 'Debe seleccionar el estado de la cita.',
            },
        }
        widgets = {
            'paciente': forms.Select(attrs={
                'class': 'form-control w-full',
            }),
            'fecha': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control w-full',
            }),
            'hora_cita': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'form-control w-full',
            }),
            'estado': forms.Select(attrs={
                'class': 'form-control w-full',
            }),
            'observaciones': forms.Textarea(attrs={
                'class': 'form-control w-full',
                'rows': 3,
                'placeholder': 'Escriba observaciones (opcional)...',
            }),
        }

    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha')
        if fecha and fecha < date.today():
            raise ValidationError("La fecha no puede estar en el pasado.")
        return fecha

    def clean(self):
        cleaned_data = super().clean()
        fecha = cleaned_data.get('fecha')
        hora = cleaned_data.get('hora_cita')
        paciente = cleaned_data.get('paciente')

        if fecha and hora:
            existe = CitaMedica.objects.filter(
                fecha=fecha,
                hora_cita=hora
            )
            if self.instance.pk:
                existe = existe.exclude(pk=self.instance.pk)

            if existe.exists():
                raise ValidationError("Ya existe una cita registrada en esa fecha y hora.")
