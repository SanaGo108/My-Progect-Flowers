from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Order, CartItem, Cart
from catalog.models import Product
import json


@login_required
def create_order(request):
    if request.method == 'POST':
        product_ids = request.POST.getlist('products')
        products = Product.objects.filter(id__in=product_ids)
        order = Order.objects.create(user=request.user)
        order.products.set(products)
        return redirect('order_history')
    return render(request, 'orders/orders.html', {'products': Product.objects.all()})


@login_required
def cart(request):
    """
    Отображает корзину текущего пользователя.
    """
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.cart_items.select_related('product')
    return render(request, 'cart.html', {'cart_items': cart_items})


@csrf_exempt
def add_to_cart(request, product_id):
    """
    Обработчик для добавления товаров в корзину.
    """
    if not request.user.is_authenticated:
        return JsonResponse({"success": False, "message": "Вы должны войти в систему для добавления товаров в корзину."})

    if request.method != 'POST':
        return JsonResponse({"success": False, "message": "Метод запроса должен быть POST."})

    product = get_object_or_404(Product, id=product_id)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"success": False, "message": "Некорректные данные."})

    quantity = data.get('quantity', 1)

    if quantity < 1:
        return JsonResponse({"success": False, "message": "Количество должно быть больше нуля."})

    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity += quantity
    else:
        cart_item.quantity = quantity

    cart_item.save()
    return JsonResponse({"success": True, "message": f"Товар '{product.name}' добавлен в корзину."})


@csrf_exempt
@login_required
def remove_from_cart(request):
    """
    Обработчик для удаления товаров из корзины.
    """
    if request.method != 'POST':
        return JsonResponse({"success": False, "message": "Метод запроса должен быть POST."})

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"success": False, "message": "Некорректные данные."})

    item_id = data.get('item_id')

    cart_item = CartItem.objects.filter(id=item_id, cart__user=request.user).first()

    if cart_item:
        cart_item.delete()
        return JsonResponse({"success": True, "message": "Товар удалён из корзины."})

    return JsonResponse({"success": False, "message": "Товар не найден."})
