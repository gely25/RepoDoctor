# applications/doctor/forms/detallepago.py

from django import forms
from applications.doctor.models import DetallePago

class DetallePagoForm(forms.ModelForm):
    class Meta:
        model = DetallePago
        fields = [
            'pago',
            'servicio_adicional',
            'cantidad',
            'precio_unitario',
            'descuento_porcentaje',
            'aplica_seguro',
            'valor_seguro',
            'descripcion_seguro',
            # 'subtotal' no se incluye porque es calculado automáticamente
        ]
        widgets = {
            'pago': forms.Select(attrs={
                'class': 'form-control',
                'autocomplete': 'off'
            }),
            'servicio_adicional': forms.Select(attrs={
                'class': 'form-control',
                'autocomplete': 'off'
            }),
            'cantidad': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese la cantidad',
                'autocomplete': 'off',
                'min': 1
            }),
            'precio_unitario': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Precio normal sin seguro',
                'step': '0.01',
                'min': '0'
            }),
            'descuento_porcentaje': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej. 10 para 10%',
                'step': '0.01',
                'min': '0',
                'max': '100'
            }),
            'aplica_seguro': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'valor_seguro': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Valor cubierto por el seguro',
                'step': '0.01',
                'min': '0'
            }),
            'descripcion_seguro': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del seguro (opcional)'
            }),
        }
        labels = {
            'pago': 'Pago',
            'servicio_adicional': 'Servicio',
            'cantidad': 'Cantidad',
            'precio_unitario': 'Precio Unitario',
            'descuento_porcentaje': 'Descuento (%)',
            'aplica_seguro': '¿Aplica Seguro?',
            'valor_seguro': 'Valor Cubierto por Seguro',
            'descripcion_seguro': 'Descripción del Seguro',
        }
        error_messages = {
            'cantidad': {
                'required': 'Debe indicar la cantidad del servicio.',
                'min_value': 'La cantidad debe ser mayor que cero.',
            },
            'precio_unitario': {
                'required': 'Ingrese el precio unitario.',
                'min_value': 'El precio no puede ser negativo.',
            },
            'descuento_porcentaje': {
                'max_value': 'El descuento no puede superar el 100%.',
                'min_value': 'El descuento no puede ser negativo.',
            },
        }
