from django.urls import path
from . import views


urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('home/', views.home, name='home'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
]
