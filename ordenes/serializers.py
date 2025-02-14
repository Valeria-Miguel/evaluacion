# serializers.py en orders
from rest_framework import serializers
from .models import Order, Client, OrderDetail
from flowers.serializers import FlowerSerializer

# Serializador para el Cliente
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

# Serializador para el Detalle de la Orden
class OrderDetailSerializer(serializers.ModelSerializer):
    flor = FlowerSerializer()  # Incluimos los detalles de la flor

    class Meta:
        model = OrderDetail
        fields = ['flor', 'cantidad', 'precio_unitario']

# Serializador para la Orden
class OrderSerializer(serializers.ModelSerializer):
    cliente = ClientSerializer()  # Información del cliente
    detalles = OrderDetailSerializer(many=True)  # Relación de flores

    class Meta:
        model = Order
        fields = ['cliente', 'fecha_creacion', 'estado', 'precio_total', 'detalles']
