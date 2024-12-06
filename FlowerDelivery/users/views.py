from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from orders.models import Order  # Импорт модели заказов
from django.db import connection

def register(request):
    """
    Регистрация нового пользователя.
    После успешной регистрации происходит автоматическая авторизация
    и перенаправление в личный кабинет.
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Авторизация пользователя
            return redirect('dashboard')  # Перенаправление в личный кабинет
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})


def dashboard(request):
    orders = request.user.orders.all()
    print(connection.queries)  # Показывает все SQL-запросы
    return render(request, 'users/dashboard.html', {'orders': orders})