from django.shortcuts import render
from . import models
from . import forms

# Create your views here.
def index(request):
    return render(request, "blog/index.html")

def post_list(request):
    posts = models.Post.objects.all()
    contexto = {"posts": posts}
    return render(request, "blog/post_list.html", contexto)

def autores_list(request):
    autores = models.Autor.objects.all()
    contexto = {"autores": autores}
    return render(request, "blog/autores_list.html", contexto)

def autores_add(request):
    if request.method == "GET":
        form = forms.AutorForm
        return render(request, "blog/autores_add.html", {"form": form})