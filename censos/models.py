from django.db import models

# Create your models here.
class Censo(models.Model):
    idestado = models.TextField(null=True)
    estado = models.TextField(null=True)
    idmunicipio = models.TextField(null=True)
    municipio = models.TextField(null=True)
    actividad = models.TextField(null=True)
    UE = models.DecimalField(max_digits=20, decimal_places=4)
    H001A= models.DecimalField(max_digits=20, decimal_places=4) 
    H010A = models.DecimalField(max_digits=20, decimal_places=4) 
    A111A = models.DecimalField(max_digits=20, decimal_places=4) 
    A211A = models.DecimalField(max_digits=20, decimal_places=4) 
    M091A = models.DecimalField(max_digits=20, decimal_places=4)
    H010D = models.DecimalField(max_digits=20, decimal_places=4) 
    H020A = models.DecimalField(max_digits=20, decimal_places=4) 
    I000A = models.DecimalField(max_digits=20, decimal_places=4) 
    I100A = models.DecimalField(max_digits=20, decimal_places=4) 
    I200A = models.DecimalField(max_digits=20, decimal_places=4) 
    K000A = models.DecimalField(max_digits=20, decimal_places=4) 
    K020A = models.DecimalField(max_digits=20, decimal_places=4) 
    K311A = models.DecimalField(max_digits=20, decimal_places=4) 
    K040A = models.DecimalField(max_digits=20, decimal_places=4) 
    K041A = models.DecimalField(max_digits=20, decimal_places=4) 
    K050A = models.DecimalField(max_digits=20, decimal_places=4) 
    K620A = models.DecimalField(max_digits=20, decimal_places=4) 
    K060A = models.DecimalField(max_digits=20, decimal_places=4) 
    K810A = models.DecimalField(max_digits=20, decimal_places=4) 
    K090A = models.DecimalField(max_digits=20, decimal_places=4) 
    A700A = models.DecimalField(max_digits=20, decimal_places=4) 
    M000A = models.DecimalField(max_digits=20, decimal_places=4) 
    M020A = models.DecimalField(max_digits=20, decimal_places=4) 
    M090A = models.DecimalField(max_digits=20, decimal_places=4) 
    A800A = models.DecimalField(max_digits=20, decimal_places=4) 

