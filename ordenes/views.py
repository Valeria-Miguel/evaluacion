from rest_framework import generics
from .models import Order, Client, OrderDetail
from .serializers import OrderSerializer, ClientSerializer
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdminOnly  #para controlar acceso

#ver las órdenes de todos los clientes administrador o empleado
class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]  #solo usuarios autenticados pueden ver

#crear una nueva orden calquier usuario autenticado puede crear
class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados 

# ver detalles 
class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]  #slo usuarios autenticados pueden ver

# modificar solo Admin o Empleado
class OrderUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsAdminOnly]  #solo admin puede modificar

# eliminar solo Admin
class OrderDeleteView(generics.DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsAdminOnly]  #solo admin puede eliminar
