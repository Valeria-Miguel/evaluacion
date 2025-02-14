from rest_framework import generics
from flowers.models import Flower
from flowers.serializers import FlowerSerializer
from users.permissions import IsAdminOrEmpleado, IsAdminOnly
from rest_framework.permissions import IsAuthenticated

#vista para listar todas las flores solo los usuarios autenticados
class FlowerListView(generics.ListAPIView):
    queryset = Flower.objects.all() #consulta para obtener todas las flores
    serializer_class = FlowerSerializer #se usara el serializador 'FlowerSerializer'
    permission_classes = [IsAuthenticated]   #solo los usuarios autenticados podran acceder

# crear una nueva florsolo admin y empleado
class FlowerCreateView(generics.CreateAPIView):
    queryset = Flower.objects.all()
    serializer_class = FlowerSerializer
    permission_classes = [IsAdminOrEmpleado]  # solo admin y empleado pueden crear

#modificar una flor solo admin y empleado
class FlowerUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Flower.objects.all()
    serializer_class = FlowerSerializer
    permission_classes = [IsAdminOrEmpleado]   # solo admin y empleado pueden crear

#eliminar flor solo admin
class FlowerDeleteView(generics.DestroyAPIView):
    queryset = Flower.objects.all()
    serializer_class = FlowerSerializer
    permission_classes = [IsAdminOnly]  #solo Admin puede eliminar
    