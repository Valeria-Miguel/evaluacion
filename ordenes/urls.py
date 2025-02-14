from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.OrderListView.as_view(), name='order-list'),  #listar 
    path('create/', views.OrderCreateView.as_view(), name='order-create'),
    path('orders/<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),  #ver 
    path('orders/<int:pk>/update/', views.OrderUpdateView.as_view(), name='order-update'),  # modificar 
    path('orders/<int:pk>/delete/', views.OrderDeleteView.as_view(), name='order-delete'),  #liminar 
]
