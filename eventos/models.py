from django.db import models
from django.utils import timezone

# Create your models here.
class evento(models.Model):    
    nombre = models.CharField(max_length=100)
    fecha_Asig = models.DateField()
    fecha_Inicio = models.DateField(default=timezone.now)
    fecha_fin = models.DateField(default=timezone.now)
    fecha_fin_asig = models.DateField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    diploma = models.BooleanField()
    activo = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/',null=True)

    def str(self):
       return self.nombre
    

tipo_contacto = [
    (1, 'No puedo Entrar'),
    (2, 'No aparece mi Evento'),
    (3, 'Otros')
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    tipo = models.IntegerField(choices=tipo_contacto)
    mensaje = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nombre