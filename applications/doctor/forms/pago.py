from django import forms
from applications.doctor.models import Pago
from django.utils import timezone
from django.core.exceptions import ValidationError

class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = [
            'atencion', 'metodo_pago', 'monto_total', 'estado',
            'fecha_pago', 'nombre_pagador', 'referencia_externa',
            'evidencia_pago', 'observaciones', 'activo'
        ]
        widgets = {
            'atencion': forms.Select(attrs={'class': 'form-control'}),
            'metodo_pago': forms.Select(attrs={'class': 'form-control'}),
            'monto_total': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'step': '0.01'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'fecha_pago': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'nombre_pagador': forms.TextInput(attrs={'class': 'form-control'}),
            'referencia_externa': forms.TextInput(attrs={'class': 'form-control'}),
            'evidencia_pago': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'atencion': 'Atención Médica',
            'metodo_pago': 'Método de Pago',
            'monto_total': 'Monto Total',
            'estado': 'Estado del Pago',
            'fecha_pago': 'Fecha de Pago',
            'nombre_pagador': 'Nombre del Pagador',
            'referencia_externa': 'Referencia Externa',
            'evidencia_pago': 'Evidencia del Pago',
            'observaciones': 'Observaciones',
            'activo': '¿Activo?',
        }
        error_messages = {
            'metodo_pago': {
                'required': 'Por favor, selecciona un método de pago.',
            },
            'monto_total': {
                'required': 'El monto total es obligatorio.',
                'invalid': 'Introduce un número válido.',
            },
            'estado': {
                'required': 'Selecciona el estado del pago.',
            },
            'fecha_pago': {
                'invalid': 'La fecha de pago no tiene un formato válido.',
            },
            'nombre_pagador': {
                'max_length': 'El nombre del pagador es demasiado largo.',
            },
            'referencia_externa': {
                'max_length': 'La referencia externa es demasiado larga.',
            },
            'evidencia_pago': {
                'invalid': 'Debes subir un archivo válido de imagen.',
            },
        }

    def clean(self):
        cleaned_data = super().clean()
        metodo_pago = cleaned_data.get('metodo_pago')
        referencia = cleaned_data.get('referencia_externa')
        evidencia = cleaned_data.get('evidencia_pago')

        if metodo_pago and metodo_pago.lower() != 'efectivo':
            if not referencia:
                self.add_error('referencia_externa', 'Este campo es obligatorio para pagos no en efectivo.')
            if not evidencia:
                self.add_error('evidencia_pago', 'Debe adjuntar una evidencia del pago no en efectivo.')

        if cleaned_data.get('fecha_pago') and cleaned_data['fecha_pago'] > timezone.now():
            self.add_error('fecha_pago', 'La fecha de pago no puede ser en el futuro.')

        return cleaned_data
