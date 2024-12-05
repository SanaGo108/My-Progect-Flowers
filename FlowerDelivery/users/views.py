from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from orders.models import Order  # Импорт модели заказов

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


@login_required
def dashboard(request):
    """
    Представление для личного кабинета пользователя.
    Показывает историю заказов текущего пользователя.
    """
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'users/templates/users/dashboard.html', {'orders': orders})
