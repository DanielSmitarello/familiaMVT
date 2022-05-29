import datetime
from django.db import models

# Create your models here.

class Familiar(models.Model):
    name = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    datebirth = models.DateField()
    edad = models.IntegerField()
    relathionship = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return f"Nombre: {self.name} Apellido: {self.lastname} Nacimiento: {self.datebirth} Edad: {self.edad} Parentesco: {self.relathionship}"