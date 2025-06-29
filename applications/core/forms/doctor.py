from django import forms
from applications.core.models import Doctor
from django.core.exceptions import ValidationError

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
        labels = {
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'ruc': 'RUC',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'direccion': 'Dirección de Trabajo',
            'latitud': 'Latitud',
            'longitud': 'Longitud',
            'codigo_unico_doctor': 'Código Único del Doctor',
            'especialidad': 'Especialidades',
            'telefonos': 'Teléfonos',
            'email': 'Correo Electrónico',
            'horario_atencion': 'Horario de Atención',
            'duracion_atencion': 'Duración de Cita (minutos)',
            'curriculum': 'Currículum Vitae',
            'firma_digital': 'Firma Digital',
            'foto': 'Foto',
            'imagen_receta': 'Imagen para Recetas',
            'activo': 'Activo',
        }
        help_texts = {
            'ruc': 'Ingrese un RUC válido (persona natural, sociedad o extranjero).',
            'direccion': 'Ubicación física donde atiende el doctor.',
            'latitud': 'Coordenada GPS (opcional).',
            'longitud': 'Coordenada GPS (opcional).',
            'codigo_unico_doctor': 'Identificador interno único para el doctor.',
            'especialidad': 'Seleccione una o más especialidades médicas.',
            'telefonos': 'Número de contacto. Puede ser celular o fijo.',
            'email': 'Correo de contacto (opcional).',
            'horario_atencion': 'Ejemplo: Lunes a Viernes, 08h00 - 13h00',
            'duracion_atencion': 'Tiempo estándar asignado a cada paciente.',
            'curriculum': 'Archivo PDF o DOC (opcional).',
            'firma_digital': 'Imagen que será usada para firmar digitalmente.',
            'imagen_receta': 'Encabezado o firma que se mostrará en recetas médicas.',
            'activo': 'Si está desmarcado, el doctor no podrá ser asignado a consultas.',
        }
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'ruc': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'latitud': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'longitud': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'codigo_unico_doctor': forms.TextInput(attrs={'class': 'form-control'}),
            'especialidad': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'telefonos': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'horario_atencion': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'duracion_atencion': forms.NumberInput(attrs={'class': 'form-control'}),
            'curriculum': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'firma_digital': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'imagen_receta': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    # Ejemplo de validación personalizada adicional (opcional)
    def clean_duracion_atencion(self):
        duracion = self.cleaned_data.get('duracion_atencion')
        if duracion < 5:
            raise ValidationError("La duración mínima de atención debe ser de al menos 5 minutos.")
        return duracion
