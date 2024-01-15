from django.shortcuts import render, redirect
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
    if request.method == "POST":
        form = forms.AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog:autores_list")
    else:
        form = forms.AutorForm
    return render(request, "blog/autores_add.html", {"form": form})
    
