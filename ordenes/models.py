from django.db import models
from flowers.models import Flower  #relacion con las flores
from django.utils import timezone

#cliente (no relacionado con los usuarios)
class Client(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.TextField()
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    creado_en = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre

# orden cada cliente puede tener muchas prdenes
class Order(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('pagado', 'Pagado'),
        ('entregado', 'Entregado'),
    ]

    cliente = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='ordenes')
    fecha_creacion = models.DateTimeField(default=timezone.now)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Orden #{self.id} - {self.cliente.nombre}"

#detalle de la orden cada orden puede tener múltiples flores
class OrderDetail(models.Model):
    orden = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='detalles')
    flor = models.ForeignKey(Flower, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cantidad} x {self.flor.nombre}"
