from django.db import models

# Create your models here.

class Medicamento(models.Model):
    id_medicamento=models.PositiveSmallIntegerField(primary_key=True)
    nombre=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=100)
    dosis=models.CharField(max_length=100)
    frecuencia=models.CharField(max_length=100)
    efectos=models.CharField(max_length=100)
    precio=models.CharField(max_length=100)

    def __str__(self):
        return self.nombre