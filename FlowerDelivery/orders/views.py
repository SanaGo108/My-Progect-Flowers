from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Order
from catalog.models import Product
import json

def create_order(request):
    if request.method == 'POST':
        product_ids = request.POST.getlist('products')
        products = Product.objects.filter(id__in=product_ids)
        order = Order.objects.create(user=request.user)
        order.products.set(products)
        return redirect('order_history')
    return render(request, 'orders/orders.html', {'products': Product.objects.all()})

def cart(request):
    return render(request, 'orders/cart.html', {'current_page': 'cart'})

@csrf_exempt
def add_to_cart(request):
    """
    Обработчик для добавления товаров в корзину.
    """
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = data.get('product_id')
        quantity = data.get('quantity')

        if not product_id or not quantity:
            return JsonResponse({"success": False, "message": "Некорректные данные."})

        # Пример обработки добавления товара в корзину:
        product = Product.objects.filter(id=product_id).first()
        if product:
            # Здесь добавьте логику работы с корзиной, например, запись в сессию или в базу данных.
            return JsonResponse({"success": True, "message": f"Товар '{product.name}' добавлен в корзину."})
        else:
            return JsonResponse({"success": False, "message": "Товар не найден."})

    return JsonResponse({"success": False, "message": "Метод запроса должен быть POST."})
