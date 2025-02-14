
from django.db import models
from users.models import CustomUser  # Importamos el modelo de usuario

class Flower(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)  # Quién creó la flor
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
