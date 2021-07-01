import uuid
from django.contrib.auth.models import User
from django.db import models

class Deporte(models.Model):
    nombre = models.CharField(max_length=100)
    img = models.ImageField()

    def __str__(self) -> str:
        return self.nombre

class Comunidad(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='ID', editable=False)
    nombre = models.CharField(max_length=150)
    deporte = models.ForeignKey('Deporte', on_delete=models.CASCADE)
    miembros = models.ManyToManyField(User, blank=True, related_name="miembros+")
    favoritos = models.ManyToManyField(User, blank=True, related_name="favoritos+")
    fecha_creacion = models.DateField(auto_now_add=True, editable=False)

class TipoZona(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    icono = models.ImageField()

class Zona(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()
    descripcion = models.CharField(max_length=150)
    tipo = models.ForeignKey('TipoZona', on_delete=models.CASCADE)

    class Meta:
        unique_together = (("lat", "lng"))

class Noticia(models.Model):
    img = models.ImageField()
    titulo = models.CharField(max_length=70)
    texto = models.CharField(max_length=150)