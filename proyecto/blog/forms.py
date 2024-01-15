from django import forms
from . import models

class AutorForm(forms.ModelForm):
    class Meta:
        model =models.Autor
        fields="__all__"

class ComentarioForm(forms.ModelForm):
    class Meta:
        model =models.Comentario
        fields="__all__"
        widgets = {'fecha_comentario': forms.DateTimeInput(attrs={'type': 'datetime-local'}),}

class PostForm(forms.ModelForm):
    class Meta:
        model =models.Post
        fields="__all__"        
