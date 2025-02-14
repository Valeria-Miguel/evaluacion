# views.py en orders
from rest_framework import generics
from .models import Order, Client, OrderDetail
from .serializers import OrderSerializer, ClientSerializer
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdminOnly  # Para controlar acceso

# Ver las órdenes de todos los clientes (Administrador o Empleado)
class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden ver

# Crear una nueva orden (Cualquier usuario autenticado puede crear)
class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden crear

# Ver detalles de una orden específica
class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden ver

# Modificar una orden (Solo Admin o Empleado)
class OrderUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsAdminOnly]  # Solo admin puede modificar

# Eliminar una orden (Solo Admin)
class OrderDeleteView(generics.DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsAdminOnly]  # Solo admin puede eliminar
