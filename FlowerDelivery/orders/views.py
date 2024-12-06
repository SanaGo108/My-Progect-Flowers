from django.shortcuts import render, redirect
from .models import Order
from catalog.models import Product

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