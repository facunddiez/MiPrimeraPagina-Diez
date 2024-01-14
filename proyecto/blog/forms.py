from django import forms
from . import models

class AutorForm(forms.ModelForm):
    class Meta:
        model =models.Autor
        fields="__all__"
