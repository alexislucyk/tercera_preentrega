from django import forms

class ClienteFormulario(forms.Form):
    apellido=forms.CharField(required=True)
    nombre=forms.CharField(required=True)
    telefono=forms.IntegerField()