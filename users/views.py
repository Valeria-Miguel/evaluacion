from rest_framework import viewsets
from .models import CustomUser
from .serializers import UserSerializer, RegisterSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework import permissions
from .permissions import IsAdminOrEmpleado  # Importamos el nuevo permiso personalizado

# Definir el permiso personalizado
class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Permiso personalizado que permite solo a los administradores modificar
    los recursos de usuario, pero todos los usuarios autenticados pueden verlos.
    """

class UserViewSet(viewsets.ModelViewSet):
    """
    vista para gestionar usuarios:
    - Viewer puede solo ver usuarios
    - Administrador y Empleado pueden crear, actualizar y eliminar usuarios
    """
    queryset = CustomUser.objects.all()  #obtiene todos los usuarios
    serializer_class = UserSerializer  #usa el serializador de usuarios
    permission_classes = [IsAdminOrEmpleado]  #aplicamos el permiso personalizado

    def get_permissions(self):
        """
        ajustamos los permisos d el metodo HTTP.
        """
        if self.action == 'list':  #acción GET Sin autenticación
            return [AllowAny()]  # permitir acceso sin autenticación
        elif self.action == 'create':  #acción POST con autenticación
            return [IsAuthenticated()]  # solo usuarios autenticados pueden crear usuarios
        else:
            return super().get_permissions()  #usar permisos por defecto para otras acciones
        

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer  #usa el serializador de registro
    permission_classes = [IsAdminOrEmpleado]  #permitir el registro sin autenticación

    def post(self, request, *args, **kwargs):
        print(request.data)  # imprimir los datos del registro para depuracion
        return super().post(request, *args, **kwargs)