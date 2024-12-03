from django.db import models

# Create your models here.

class Medico(models.Model):
    idmedico=models.PositiveSmallIntegerField(primary_key=True)
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    especialidad=models.CharField(max_length=100)
    telefono=models.CharField(max_length=100)
    correo=models.CharField(max_length=100)
    fechadecontratacion=models.DateField()

    def __str__(self):
        return self.nombre_empresa
