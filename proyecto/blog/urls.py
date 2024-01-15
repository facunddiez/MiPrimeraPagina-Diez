
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    
    path("autores/list", views.autores_list, name="autores_list"),
    path("blog/add", views.autores_add, name="autores_add"),
    path("blog/autores", views.autores, name="autores"),
    path("blog/post_add", views.post_add, name="post_add"),
    path("blog/list", views.post_list, name="post_list"),
    path("blog/comentarios", views.comentarios, name="comentarios"),
    path("comentarios/comentarios_list", views.comentarios_list, name="comentarios_list"),
    path("comentarios/comentarios_add", views.comentarios_add, name="comentarios_add"),

]