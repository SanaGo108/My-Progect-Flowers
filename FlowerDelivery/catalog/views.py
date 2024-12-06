from django.shortcuts import render
from .models import Product

def catalog(request):
    products = Product.objects.all()
    return render(request, 'catalog/catalog.html', {
        'products': products,
        'current_page': 'catalog',  # Передача переменной current_page
    })

def home(request):
    return render(request, 'home.html', {'current_page': 'home'})