from django import forms
from applications.doctor.models import HorarioAtencion
from django.utils.translation import gettext_lazy as _

class HorarioAtencionForm(forms.ModelForm):
    class Meta:
        model = HorarioAtencion
        fields = ['dia_semana', 'hora_inicio', 'hora_fin', 'intervalo_desde', 'intervalo_hasta', 'activo']
        labels = {
            'dia_semana': 'Día de la Semana',
            'hora_inicio': 'Hora de Inicio',
            'hora_fin': 'Hora de Fin',
            'intervalo_desde': 'Intervalo Desde',
            'intervalo_hasta': 'Intervalo Hasta',
            'activo': '¿Activo?',
        }
        widgets = {
            'dia_semana': forms.Select(attrs={'class': 'form-control'}),
            'hora_inicio': forms.TimeInput(format='%H:%M', attrs={'type': 'time', 'class': 'form-control'}),
            'hora_fin': forms.TimeInput(format='%H:%M', attrs={'type': 'time', 'class': 'form-control'}),
            'intervalo_desde': forms.TimeInput(format='%H:%M', attrs={'type': 'time', 'class': 'form-control'}),
            'intervalo_hasta': forms.TimeInput(format='%H:%M', attrs={'type': 'time', 'class': 'form-control'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        error_messages = {
            'dia_semana': {
                'required': 'Debe seleccionar un día.',
            },
            'hora_inicio': {
                'required': 'Debe ingresar la hora de inicio.',
            },
            'hora_fin': {
                'required': 'Debe ingresar la hora de fin.',
            },
        }

    def clean_hora_fin(self):
        hora_inicio = self.cleaned_data.get('hora_inicio')
        hora_fin = self.cleaned_data.get('hora_fin')
        if hora_inicio and hora_fin and hora_fin <= hora_inicio:
            raise forms.ValidationError("La hora de fin debe ser posterior a la hora de inicio.")
        return hora_fin

    def clean_intervalo_hasta(self):
        intervalo_desde = self.cleaned_data.get('intervalo_desde')
        intervalo_hasta = self.cleaned_data.get('intervalo_hasta')
        if intervalo_desde and intervalo_hasta and intervalo_hasta <= intervalo_desde:
            raise forms.ValidationError("El intervalo hasta debe ser posterior al intervalo desde.")
        return intervalo_hasta

    def clean(self):
        cleaned_data = super().clean()
        hora_inicio = cleaned_data.get('hora_inicio')
        hora_fin = cleaned_data.get('hora_fin')
        intervalo_desde = cleaned_data.get('intervalo_desde')
        intervalo_hasta = cleaned_data.get('intervalo_hasta')

        if intervalo_desde and (intervalo_desde <= hora_inicio or intervalo_desde >= hora_fin):
            self.add_error('intervalo_desde', 'El intervalo debe estar dentro del horario de atención.')

        if intervalo_hasta and (intervalo_hasta <= hora_inicio or intervalo_hasta >= hora_fin):
            self.add_error('intervalo_hasta', 'El intervalo debe estar dentro del horario de atención.')

        return cleaned_data
