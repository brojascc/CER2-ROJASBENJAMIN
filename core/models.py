from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    # id = models.UUIDField(primary_key=True, editable=False)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    
    
class LugarPatrimonial(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=255)
    anio_construccion = models.IntegerField(null=True, blank=True)
    imagen = models.URLField(null=True, blank=True, max_length=500)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    