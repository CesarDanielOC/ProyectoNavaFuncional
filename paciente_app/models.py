from django.db import models

class Paciente(models.Model):
    id_paciente = models.PositiveSmallIntegerField(primary_key=True)  
    nombre = models.CharField(max_length=100)  
    apellidos = models.CharField(max_length=100)  
    fechanacimiento = models.DateField()  
    telefono = models.CharField(max_length=100) 
    direccion = models.CharField(max_length=100) 
    fecharegistro = models.DateField()  

    def __str__(self):
        return self.nombre
