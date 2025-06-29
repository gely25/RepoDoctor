# core/forms/atencion.py

from django import forms
from applications.doctor.models import Atencion

class AtencionForm(forms.ModelForm):
    class Meta:
        model = Atencion
        fields = [
            'paciente', 'presion_arterial', 'pulso', 'temperatura', 'frecuencia_respiratoria',
            'saturacion_oxigeno', 'peso', 'altura', 'motivo_consulta', 'sintomas',
            'tratamiento', 'diagnostico', 'examen_fisico', 'examenes_enviados',
            'comentario_adicional', 'es_control'
        ]
        widgets = {
            'paciente': forms.Select(attrs={
                'class': 'form-control rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-500 focus:ring-opacity-50'
            }),
            'presion_arterial': forms.TextInput(attrs={
                'placeholder': 'Ej: 120/80 mmHg',
                'class': 'form-control'
            }),
            'pulso': forms.NumberInput(attrs={'placeholder': 'Ej: 72'}),
            'temperatura': forms.NumberInput(attrs={'step': '0.1', 'placeholder': 'Ej: 36.5'}),
            'frecuencia_respiratoria': forms.NumberInput(attrs={'placeholder': 'Ej: 16'}),
            'saturacion_oxigeno': forms.NumberInput(attrs={'step': '0.01', 'placeholder': 'Ej: 98.5'}),
            'peso': forms.NumberInput(attrs={'step': '0.01', 'placeholder': 'Ej: 65.50'}),
            'altura': forms.NumberInput(attrs={'step': '0.01', 'placeholder': 'Ej: 1.70'}),
            'motivo_consulta': forms.Textarea(attrs={'rows': 3}),
            'sintomas': forms.Textarea(attrs={'rows': 3}),
            'tratamiento': forms.Textarea(attrs={'rows': 3}),
            'diagnostico': forms.SelectMultiple(attrs={
                'class': 'form-control select2'
            }),
            'examen_fisico': forms.Textarea(attrs={'rows': 3}),
            'examenes_enviados': forms.Textarea(attrs={'rows': 3}),
            'comentario_adicional': forms.Textarea(attrs={'rows': 3}),
            'es_control': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'paciente': 'Paciente',
            'presion_arterial': 'Presión Arterial',
            'pulso': 'Pulso (ppm)',
            'temperatura': 'Temperatura (°C)',
            'frecuencia_respiratoria': 'Frecuencia Respiratoria (rpm)',
            'saturacion_oxigeno': 'Saturación de Oxígeno (%)',
            'peso': 'Peso (kg)',
            'altura': 'Altura (m)',
            'motivo_consulta': 'Motivo de Consulta',
            'sintomas': 'Síntomas',
            'tratamiento': 'Plan de Tratamiento',
            'diagnostico': 'Diagnósticos',
            'examen_fisico': 'Examen Físico',
            'examenes_enviados': 'Exámenes Solicitados',
            'comentario_adicional': 'Comentario Adicional',
            'es_control': '¿Es consulta de control?',
        }
        error_messages = {
            'paciente': {
                'required': 'Debe seleccionar un paciente para la atención.',
            },
            'motivo_consulta': {
                'required': 'Debe indicar el motivo de consulta.',
            },
            'sintomas': {
                'required': 'Debe describir los síntomas del paciente.',
            },
            'tratamiento': {
                'required': 'Debe ingresar el plan de tratamiento.',
            },
            'diagnostico': {
                'required': 'Debe seleccionar al menos un diagnóstico.',
            },
        }

    def clean_temperatura(self):
        temperatura = self.cleaned_data.get('temperatura')
        if temperatura and not (30 <= temperatura <= 45):
            raise forms.ValidationError("La temperatura debe estar entre 30°C y 45°C.")
        return temperatura

    def clean_pulso(self):
        pulso = self.cleaned_data.get('pulso')
        if pulso and (pulso < 30 or pulso > 200):
            raise forms.ValidationError("El pulso debe estar entre 30 y 200 ppm.")
        return pulso

    def clean_frecuencia_respiratoria(self):
        freq = self.cleaned_data.get('frecuencia_respiratoria')
        if freq and (freq < 10 or freq > 40):
            raise forms.ValidationError("La frecuencia respiratoria debe estar entre 10 y 40 rpm.")
        return freq

    def clean_saturacion_oxigeno(self):
        sat = self.cleaned_data.get('saturacion_oxigeno')
        if sat and (sat < 70 or sat > 100):
            raise forms.ValidationError("La saturación de oxígeno debe estar entre 70% y 100%.")
        return sat

    def clean_altura(self):
        altura = self.cleaned_data.get('altura')
        if altura and altura <= 0:
            raise forms.ValidationError("La altura debe ser mayor a 0.")
        return altura

    def clean_peso(self):
        peso = self.cleaned_data.get('peso')
        if peso and peso <= 0:
            raise forms.ValidationError("El peso debe ser mayor a 0.")
        return peso
