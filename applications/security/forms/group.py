from django import forms
from django.contrib.auth.models import Group

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']
        labels = {'name': 'Nombre del grupo'}
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese nombre del grupo',
            })
        }
