from django import forms

from cliente.models import Oil

class OilForm (forms.ModelForm):

    class Meta:
        model = Oil

        fields = [
            'nombre',
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

class CurrentOilPrice (forms.Form):
    lenguaje = forms.CharField(max_length = 2)

class GetOilPrice (forms.Form):
    lenguaje = forms.CharField(max_length = 2)
    dia = forms.IntegerField()
    mes = forms.IntegerField()
    anio = forms.IntegerField()
    
