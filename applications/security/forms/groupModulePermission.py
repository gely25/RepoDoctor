import re
from django import forms
from django.forms import ModelForm

from applications.security.models import GroupModulePermission, Module

class GroupModulePermissionForm(ModelForm):
    class Meta:
        model = GroupModulePermission
        fields = [
            "group",
            "module",
            "permissions",
        ]
        error_messages = {
            "group": {
                "required": "El campo grupo es obligatorio.",
            },
            "module": {
                "required": "El campo módulo es obligatorio.",
            },
            "permissions": {
                "required": "Debe seleccionar al menos un permiso.",
            },
        }
        widgets = {
            "group": forms.Select(attrs={
                "class": "form-control"
            }),
            "module": forms.Select(attrs={
                "class": "form-control"
            }),
            "permissions": forms.CheckboxSelectMultiple(),
        }
        labels = {
            "group": "Grupo",
            "module": "Módulo",
            "permissions": "Permisos",
        }

    def clean_module(self):
        module = self.cleaned_data.get("module")
        if not Module.objects.filter(id=module.id).exists():
            raise forms.ValidationError("El módulo seleccionado no existe.")
        return module

    def clean_permissions(self):
        permissions = self.cleaned_data.get("permissions")
        if not permissions:
            raise forms.ValidationError("Debe seleccionar al menos un permiso.")
        return permissions
    
    def clean_group(self):
        group = self.cleaned_data.get("group")
        if not group:
            raise forms.ValidationError("El campo grupo es obligatorio.")
        return group
    