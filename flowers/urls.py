from django.urls import path
from flowers.views import (
    FlowerListView, FlowerCreateView, 
    FlowerUpdateView, FlowerDeleteView
)

urlpatterns = [
    path('list/', FlowerListView.as_view(), name='flower-list'),  # Solo ver
    path('create/', FlowerCreateView.as_view(), name='flower-create'),  # Solo crear
    path('update/<int:pk>/', FlowerUpdateView.as_view(), name='flower-update'),  # Modificar
    path('delete/<int:pk>/', FlowerDeleteView.as_view(), name='flower-delete'),  # Eliminar
]
