from django.db import models

class Colectividad(models.Model):
    nombre = models.CharField(max_length=100) 
    pais = models.CharField(max_length=100)  
    
    def __str__(self):
        return f'Colectividad ({self.id}): {self.nombre} - {self.pais}'
