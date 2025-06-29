from django import forms
from applications.core.models import Medicamento, TipoMedicamento, MarcaMedicamento
from django.core.exceptions import ValidationError

class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = '__all__'
        widgets = {
            'tipo': forms.Select(attrs={
                'class': 'w-full rounded-lg border border-gray-300 p-2.5 dark:bg-secundario dark:text-white'
            }),
            'marca_medicamento': forms.Select(attrs={
                'class': 'w-full rounded-lg border border-gray-300 p-2.5 dark:bg-secundario dark:text-white'
            }),
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Ejemplo: Ibuprofeno',
                'class': 'w-full rounded-lg border border-gray-300 p-2.5 dark:bg-secundario dark:text-white'
            }),
            'descripcion': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Escriba indicaciones, usos, precauciones...',
                'class': 'w-full rounded-lg border border-gray-300 p-2.5 dark:bg-secundario dark:text-white'
            }),
            'concentracion': forms.TextInput(attrs={
                'placeholder': 'Ejemplo: 500mg, 5%',
                'class': 'w-full rounded-lg border border-gray-300 p-2.5 dark:bg-secundario dark:text-white'
            }),
            'via_administracion': forms.Select(attrs={
                'class': 'w-full rounded-lg border border-gray-300 p-2.5 dark:bg-secundario dark:text-white'
            }),
            'cantidad': forms.NumberInput(attrs={
                'class': 'w-full rounded-lg border border-gray-300 p-2.5 dark:bg-secundario dark:text-white'
            }),
            'precio': forms.NumberInput(attrs={
                'step': '0.01',
                'class': 'w-full rounded-lg border border-gray-300 p-2.5 dark:bg-secundario dark:text-white'
            }),
            'comercial': forms.CheckboxInput(attrs={
                'class': 'rounded text-blue-600 focus:ring-blue-500 dark:focus:ring-blue-400'
            }),
            'activo': forms.CheckboxInput(attrs={
                'class': 'rounded text-green-600 focus:ring-green-500 dark:focus:ring-green-400'
            }),
            'foto': forms.ClearableFileInput(attrs={
                'class': 'w-full border-gray-300 dark:bg-secundario dark:text-white file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100'
            }),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if len(nombre) < 3:
            raise ValidationError("El nombre del medicamento debe tener al menos 3 caracteres.")
        return nombre

    def clean_precio(self):
        precio = self.cleaned_data['precio']
        if precio <= 0:
            raise ValidationError("El precio debe ser mayor que cero.")
        return precio

    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 0:
            raise ValidationError("La cantidad no puede ser negativa.")
        return cantidad
