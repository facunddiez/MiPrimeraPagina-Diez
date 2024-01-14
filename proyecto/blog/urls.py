
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("post/list", views.post_list, name="post_list"),
    path("autores/list", views.autores_list, name="autores_list"),
]