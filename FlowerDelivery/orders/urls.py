from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_order, name='create_order'),
    path('cart/', views.cart, name='cart'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),  # Исправлено
]
