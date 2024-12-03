from django.db import models

# Create your models here.

class Citas(models.Model):
    idcita=models.PositiveSmallIntegerField(primary_key=True)
    idpaciente=models.CharField(max_length=100)
    idmedico=models.CharField(max_length=100)
    fechacita=models.DateField()
    horacita=models.TimeField()
    motivo=models.CharField(max_length=100)
    estado=models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion
