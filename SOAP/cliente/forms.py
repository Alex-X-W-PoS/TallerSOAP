from django import forms

from cliente.models import Oil

class OilForm (forms.ModelForm):

    class Meta:
        model = Oil

        fields = [
            'nombre'
            'fecha_emision',
            'precio',
        ]
        labels = {
            'nombre': 'Nombre del producto',
            'fecha_emision': 'Fecha de Elaboracion',
            'precio': 'Precio',
        }
        widgets = {
            'nombre': forms.TextInput(),
            'fecha_emision': forms.DateInput(),
            'precio': forms.NumberInput(),
        }