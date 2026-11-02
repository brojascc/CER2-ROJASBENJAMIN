from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    # id = models.UUIDField(primary_key=True, editable=False)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    
    
class LugarPatrimonial(models.Model):
    # id = models.UUIDField(primary_key=True, editable=False)
    nombre = models.TextField()
    descripcion = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    anio_construccion = models.DateField()
    imagen = models.URLField(null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    