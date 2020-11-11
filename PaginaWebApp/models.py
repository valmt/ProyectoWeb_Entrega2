from django.db import models
from .rutificador import validate_rutificador

class Cliente(models.Model)  :
    nombre   = models.TextField(max_length=20)
    apellido = models.TextField(max_length=20)
    rut      = models.TextField(max_length=12, validators=[validate_rutificador])

    def __str__(self)   :
        return self.nombre +" "+ self.apellido

class GiftCard(models.Model):
    numeroTarjeta   = models.TextField(max_length=12)
    saldoDisponible = models.IntegerField()
    rut             = models.TextField(max_length=12, validators=[validate_rutificador])
    clave           = models.TextField(max_length=4)

    def __str__(self) :
        return self.rut + " " + self.numeroTarjeta
