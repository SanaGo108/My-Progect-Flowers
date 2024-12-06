from django.shortcuts import render
from .models import Product
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def catalog(request):
    products = Product.objects.all()
    return render(request, 'catalog/catalog.html', {
        'products': products,
        'current_page': 'catalog',  # Передача переменной current_page
    })

def home(request):
    return render(request, 'home.html', {'current_page': 'home'})

@csrf_exempt
def add_to_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = data.get('product_id')
        quantity = data.get('quantity')

        # Логика добавления товара в корзину
        # Например, создание записи в модели CartItem
        if product_id and quantity:
            # Здесь добавьте проверку, существует ли продукт
            return JsonResponse({"success": True, "message": "Товар добавлен в корзину."})
        return JsonResponse({"success": False, "message": "Некорректные данные."})
    return JsonResponse({"success": False, "message": "Только POST-запросы."})

def cart_view(request):
    # Здесь логика отображения корзины
    return render(request, 'orders/cart.html', {})
