from django.contrib import admin
from .models import Post, Comentario, Autor
# Register your models here.
admin.site.register(Post)
admin.site.register(Autor)
admin.site.register(Comentario)