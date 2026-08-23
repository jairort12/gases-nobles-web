from django import forms
from django.utils.translation import gettext_lazy as _

class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=100, label=_( 'Tu Nombre'))
    correo = forms.EmailField(label=_( 'Tu Correo'))
    mensaje = forms.CharField(widget=forms.Textarea, label=_( 'Mensaje'))