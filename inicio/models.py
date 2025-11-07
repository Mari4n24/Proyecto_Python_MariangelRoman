from django.db import models

class Colectividad(models.Model):
    nombre = models.CharField(max_length=100)  # Ej: "Pedro"
    pais = models.CharField(max_length=100)    # Ej: "Venezuela"

    def __str__(self):
        return self.nombre