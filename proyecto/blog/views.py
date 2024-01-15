from django.shortcuts import render, redirect
from . import models
from . import forms

# Create your views here.
def index(request):
    return render(request, "blog/index.html")

def autores(request):
    return render(request, "blog/autores.html")

def comentarios(request):
    return render(request, "blog/comentarios.html")


def post_list(request):
    posts = models.Post.objects.all()
    contexto = {"posts": posts}
    return render(request, "blog/post_list.html", contexto)

def autores_list(request):
    autores = models.Autor.objects.all()
    contexto = {"autores": autores}
    return render(request, "blog/autores_list.html", contexto)

def autores_add(request):
    if request.method == "POST":
        form = forms.AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog:autores_list")
    else:
        form = forms.AutorForm
    return render(request, "blog/autores_add.html", {"form": form})
    
def post_add(request):
    if request.method == "POST":
        form = forms.PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog:post_list")
    else:
        form = forms.PostForm
    return render(request, "blog/post_add.html", {"form": form})

def comentarios_list(request):
    comentario = models.Comentario.objects.all()
    contexto = {"comentario": comentario}
    return render(request, "blog/comentarios_list.html", contexto)

def comentarios_add(request):
    if request.method == "POST":
        form = forms.ComentarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog:comentarios_list")
    else:
        form = forms.ComentarioForm
    return render(request, "blog/comentarios_add.html", {"form": form})
