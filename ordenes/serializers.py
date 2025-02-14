from rest_framework import serializers
from .models import Order, Client, OrderDetail
from flowers.serializers import FlowerSerializer

#serializador para el cliente
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

#serializador para el Detalle de la orden
class OrderDetailSerializer(serializers.ModelSerializer):
    flor = FlowerSerializer()  # incluimos los detalles de la flor

    class Meta:
        model = OrderDetail
        fields = ['flor', 'cantidad', 'precio_unitario']

#serializador para la orden
class OrderSerializer(serializers.ModelSerializer):
    cliente = ClientSerializer()  # informacion del cliente
    detalles = OrderDetailSerializer(many=True)  #relaci´on de flores

    class Meta:
        model = Order
        fields = ['cliente', 'fecha_creacion', 'estado', 'precio_total', 'detalles']
