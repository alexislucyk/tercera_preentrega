from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from.models import Cliente

#class ClienteFormulario(forms.Form):
#    apellido=forms.CharField(required=True)
#    nombre=forms.CharField(required=True)
#    telefono=forms.IntegerField()

class ClienteFormulario(forms.ModelForm):

    class Meta:
        model=Cliente
        fields=('__all__')

class ProductoFormulario(forms.Form):
    codigo=forms.CharField(required=True)
    descripcion=forms.CharField(required=True)
    precio=forms.IntegerField()

class UserEditForm(UserChangeForm):

    password=forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
        )
    
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita Contraseña', widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=('email', 'first_name', 'last_name', 'password1', 'password2')

    def clean_password2(self):
        print(self.cleaned_data)

        pwd2 = self.cleaned_data['password2']
        if pwd2 != self.cleaned_data['password1']:
            raise forms.ValidationError('Las contraseñas son distintas.')
        return pwd2