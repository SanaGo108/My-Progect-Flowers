from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),  # Регистрация
    path('dashboard/', views.dashboard, name='dashboard'),  # Личный кабинет
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),  # Вход
]

