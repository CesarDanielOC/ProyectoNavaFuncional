from django.db import models

class Receta(models.Model):
    idreceta=models.PositiveSmallIntegerField(primary_key=True)
    idpaciente=models.CharField(max_length=100)
    idmedico=models.CharField(max_length=100)
    fechareceta=models.DateField()
    instrucciones=models.CharField(max_length=100)
    validez=models.CharField(max_length=100)
    idmedicamento=models.CharField(max_length=100)

    def __str__(self):
        return str(self.idreceta)
