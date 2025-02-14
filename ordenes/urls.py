# urls.py en orders
from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.OrderListView.as_view(), name='order-list'),  # Listar todas las órdenes
    path('create/', views.OrderCreateView.as_view(), name='order-create'),
    path('orders/<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),  # Ver detalles de una orden
    path('orders/<int:pk>/update/', views.OrderUpdateView.as_view(), name='order-update'),  # Modificar una orden
    path('orders/<int:pk>/delete/', views.OrderDeleteView.as_view(), name='order-delete'),  # Eliminar una orden
]
