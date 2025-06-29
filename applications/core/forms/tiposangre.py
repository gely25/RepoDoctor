from django import forms
from django.forms import ModelForm
from applications.core.models import TipoSangre

class TipoSangreForm(ModelForm):
    class Meta:
        model = TipoSangre
        fields = ["tipo", "descripcion"]

        error_messages = {
            "tipo": {
                "unique": "Este tipo de sangre ya está registrado.",
                "required": "El tipo de sangre es obligatorio.",
            },
            
            "descripcion": {
                "required": "La descripción es obligatoria"
                
            }
            
        }

        widgets = {
            "tipo": forms.TextInput(attrs={
                "placeholder": "Ej. A+, O-, AB-",
                "id": "id_tipo",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg "
                         "focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 "
                         "dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 "
                         "dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }),
            
            "descripcion": forms.Textarea(attrs={
                "placeholder": "Ej. Compatible con A+ y AB+. Donante universal.",
                "rows": 3,
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg "
                         "focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 "
                         "dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 "
                         "dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                
            })
        }

        labels = {
            "tipo": "Tipo de Sangre",
            "descripcion": "Descripción"
        }

    def clean_tipo(self):
        tipo= self.cleaned_data["tipo"].upper()
        if TipoSangre.objects.filter(tipo__iexact=tipo).exists():
            raise forms.ValidationError("Este tipo de sangre ya está registrado.")
        return tipo
    
    
    # Validación cruzada (entre campos)
    def clean(self):
        cleaned_data= super().clean()
        tipo= cleaned_data.get("tipo", "").strip().lower()
        descripcion= cleaned_data.get("descripcion", "").strip().lower()
        

        if tipo and descripcion and tipo == descripcion:
            self.add_error("descripcion", "La descripción no debe repetir el tipo de sangre.")


