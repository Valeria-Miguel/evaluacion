from rest_framework import generics
from flowers.models import Flower
from flowers.serializers import FlowerSerializer
from users.permissions import IsAdminOrEmpleado, IsAdminOnly
from rest_framework.permissions import IsAuthenticated

# Ver flores (todos los autenticados)
class FlowerListView(generics.ListAPIView):
    queryset = Flower.objects.all()
    serializer_class = FlowerSerializer
    permission_classes = [IsAuthenticated]  # Todos los autenticados pueden ver

# Crear flor (solo admin y empleado)
class FlowerCreateView(generics.CreateAPIView):
    queryset = Flower.objects.all()
    serializer_class = FlowerSerializer
    permission_classes = [IsAdminOrEmpleado]  # Solo Admin y Empleado pueden crear

# Modificar flor (solo admin y empleado)
class FlowerUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Flower.objects.all()
    serializer_class = FlowerSerializer
    permission_classes = [IsAdminOrEmpleado]  # Solo Admin y Empleado pueden modificar

# Eliminar flor (solo admin)
class FlowerDeleteView(generics.DestroyAPIView):
    queryset = Flower.objects.all()
    serializer_class = FlowerSerializer
    permission_classes = [IsAdminOnly]  # Solo Admin puede eliminar