from django import forms
from applications.core.models import Diagnostico
from django.core.exceptions import ValidationError

class DiagnosticoForm(forms.ModelForm):
    class Meta:
        model = Diagnostico
        fields = ['codigo', 'descripcion', 'datos_adicionales', 'activo']

        labels = {
            'codigo': 'Código del Diagnóstico',
            'descripcion': 'Descripción',
            'datos_adicionales': 'Datos Adicionales',
            'activo': 'Activo',
        }

        widgets = {
            'codigo': forms.TextInput(attrs={
                'placeholder': 'Ejemplo: A09, J00, K35.2',
                'id': 'id_codigo',
                'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg '
                         'focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 '
                         'dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 '
                         'dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light',
            }),
            'descripcion': forms.TextInput(attrs={
                'placeholder': 'Ejemplo: Faringitis aguda',
                'id': 'id_descripcion',
                'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg '
                         'focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 '
                         'dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 '
                         'dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light',
            }),
            'datos_adicionales': forms.Textarea(attrs={
                'placeholder': 'Observaciones clínicas, contexto, etc.',
                'rows': 3,
                'id': 'id_datos_adicionales',
                'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg '
                         'focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 '
                         'dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 '
                         'dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light',
            }),
            'activo': forms.CheckboxInput(attrs={
                'class': 'rounded text-green-600 focus:ring-green-500 dark:focus:ring-green-400'
            }),
        }

        error_messages = {
            'codigo': {
                'unique': 'Ya existe un diagnóstico con este código.',
                'required': 'El código del diagnóstico es obligatorio.',
            },
            'descripcion': {
                'required': 'La descripción es obligatoria.',
            },
        }

    def clean_codigo(self):
        codigo = self.cleaned_data.get('codigo', '').strip().upper()
        if len(codigo) < 2:
            raise ValidationError("El código debe tener al menos 2 caracteres.")
        return codigo

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion', '').strip()
        if len(descripcion) < 3:
            raise ValidationError("La descripción debe tener al menos 3 caracteres.")
        return descripcion
