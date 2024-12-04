from django.shortcuts import render
from .models import Product
import django.conf.urls.static


def catalog(request):
    products = Product.objects.all()
    return render(request, 'catalog/catalog.html', {'products': products})

def home(request):
    return render(request, 'home.html', {'current_page': 'home'})