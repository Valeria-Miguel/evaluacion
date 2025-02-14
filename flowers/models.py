
from django.db import models
from users.models import CustomUser  # importamos el modelo de usuario

class Flower(models.Model):
    # campo para la flor (caracterisitcas)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2) #aximo de 10 digitos en total y 2 decimales
    stock = models.PositiveIntegerField() 
    description = models.TextField(blank=True, null=True) # que puede ser opcional
     # campo que establece quien creo la flor, con referencia al modelo 'CustomUser'
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)  # Quién creó la flor
    created_at = models.DateTimeField(auto_now_add=True) #la fecha de creacion de la flor

    def __str__(self):
        return self.name
