
from django.urls import path, include
from .views import RegisterView, UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet)  #endpoint para usuarios

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  #ruta de registro
    path('', include(router.urls)),  #incluye las rutas de ViewSets
]
