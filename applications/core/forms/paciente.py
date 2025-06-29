from django import forms
from applications.core.models import Paciente
from django.core.exceptions import ValidationError

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
        labels = {
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'cedula_ecuatoriana': 'Cédula',
            'dni': 'DNI Internacional',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'telefono': 'Teléfono(s)',
            'email': 'Correo Electrónico',
            'sexo': 'Sexo',
            'estado_civil': 'Estado Civil',
            'direccion': 'Dirección Domiciliaria',
            'latitud': 'Latitud',
            'longitud': 'Longitud',
            'tipo_sangre': 'Tipo de Sangre',
            'foto': 'Foto',
            'antecedentes_personales': 'Antecedentes Personales',
            'antecedentes_quirurgicos': 'Antecedentes Quirúrgicos',
            'antecedentes_familiares': 'Antecedentes Familiares',
            'alergias': 'Alergias',
            'medicamentos_actuales': 'Medicamentos Actuales',
            'habitos_toxicos': 'Hábitos Tóxicos',
            'vacunas': 'Vacunas',
            'antecedentes_gineco_obstetricos': 'Antecedentes Gineco-Obstétricos',
            'activo': 'Paciente Activo',
        }
        help_texts = {
            'cedula_ecuatoriana': 'Ingrese el número de cédula sin espacios ni guiones.',
            'dni': 'Pasaporte, DNI, CURP u otro documento válido internacionalmente.',
            'telefono': 'Puede ingresar uno o más números separados por coma.',
            'email': 'Correo electrónico del paciente (opcional).',
            'fecha_nacimiento': 'Formato: AAAA-MM-DD',
            'latitud': 'Coordenada geográfica (opcional).',
            'longitud': 'Coordenada geográfica (opcional).',
            'foto': 'Imagen de perfil del paciente (opcional).',
            'antecedentes_personales': 'Ej.: Diabetes tipo 2, hipertensión, etc.',
            'antecedentes_quirurgicos': 'Ej.: Apendicectomía, cesárea, etc.',
            'antecedentes_familiares': 'Ej.: Padre con diabetes, madre con hipertensión.',
            'alergias': 'Ej.: Penicilina, mariscos, polvo, etc.',
            'medicamentos_actuales': 'Ej.: Metformina 850mg cada 12h.',
            'habitos_toxicos': 'Ej.: Tabaco, alcohol, drogas.',
            'vacunas': 'Ej.: COVID-19, influenza, etc.',
            'antecedentes_gineco_obstetricos': 'Solo si aplica. Ej.: menarquia, embarazos.',
        }
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'cedula_ecuatoriana': forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'estado_civil': forms.Select(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'latitud': forms.NumberInput(attrs={'class': 'form-control'}),
            'longitud': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo_sangre': forms.Select(attrs={'class': 'form-control'}),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'antecedentes_personales': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'antecedentes_quirurgicos': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'antecedentes_familiares': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'alergias': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'medicamentos_actuales': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'habitos_toxicos': forms.TextInput(attrs={'class': 'form-control'}),
            'vacunas': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'antecedentes_gineco_obstetricos': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and Paciente.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
            raise ValidationError("Este correo ya está registrado para otro paciente.")
        return email

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if telefono and len(telefono) < 7:
            raise ValidationError("Ingrese al menos 7 dígitos de teléfono.")
        return telefono
