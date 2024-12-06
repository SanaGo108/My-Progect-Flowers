from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from django.contrib.auth import views as auth_views
from users.views import dashboard  # Убедитесь, что этот метод существует

# Представление для главной страницы
def home(request):
    return render(request, 'home.html', {'current_page': 'home'})

urlpatterns = [
    path('admin/', admin.site.urls),  # Административный интерфейс
    path('users/', include('users.urls')),  # URL-ы приложения users
    path('catalog/', include('catalog.urls')),  # URL-ы приложения catalog
    path('orders/', include('orders.urls')),  # URL-ы приложения orders
    path('reviews/', include('reviews.urls')),  # URL-ы приложения reviews
    path('analytics/', include('analytics.urls')),  # URL-ы приложения analytics
    path('dashboard/', dashboard, name='dashboard'),  # Личный кабинет
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),  # Маршрут для входа
    path('', home, name='home'),  # Главная страница
    path('', include('catalog.urls')),  # Например, для главной страницы
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
