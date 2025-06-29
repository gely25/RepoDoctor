from django import forms
from applications.core.models import GastoMensual, TipoGasto

class GastoMensualForm(forms.ModelForm):
    class Meta:
        model = GastoMensual
        fields = ['tipo_gasto', 'fecha', 'valor', 'observacion']
        labels = {
            'tipo_gasto': 'Tipo de Gasto',
            'fecha': 'Fecha del Gasto',
            'valor': 'Valor en dólares',
            'observacion': 'Observación (opcional)',
        }
        widgets = {
            'tipo_gasto': forms.Select(attrs={
                'class': 'form-control dark:bg-gray-900 dark:text-white rounded-xl'
            }),
            'fecha': forms.DateInput(attrs={
                'class': 'form-control dark:bg-gray-900 dark:text-white rounded-xl',
                'type': 'date'
            }),
            'valor': forms.NumberInput(attrs={
                'class': 'form-control dark:bg-gray-900 dark:text-white rounded-xl',
                'step': '0.01',
                'min': '0'
            }),
            'observacion': forms.Textarea(attrs={
                'class': 'form-control dark:bg-gray-900 dark:text-white rounded-xl',
                'rows': 3,
                'placeholder': 'Ej. Pago de electricidad...'
            }),
        }
        error_messages = {
            'tipo_gasto': {
                'required': 'Debes seleccionar un tipo de gasto.',
                'invalid_choice': 'El tipo de gasto seleccionado no es válido.',
            },
            'fecha': {
                'required': 'Debes indicar la fecha del gasto.',
                'invalid': 'La fecha ingresada no es válida.',
            },
            'valor': {
                'required': 'El valor del gasto es obligatorio.',
                'invalid': 'El valor ingresado no es un número válido.',
            },
        }

    def clean_valor(self):
        valor = self.cleaned_data.get('valor')
        if valor is not None and valor <= 0:
            raise forms.ValidationError("El valor del gasto debe ser mayor a 0.")
        return valor
