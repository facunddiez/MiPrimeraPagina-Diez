from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.ForeignKey('Autor', on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    
class Comentario(models.Model):
    post = models.ForeignKey('Post', null=True, blank =True, on_delete=models.SET_NULL)
    autor = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_comentario = models.DateTimeField('Fecha de comentario')

    def __str__(self):
        return self.contenido
    
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.nombre