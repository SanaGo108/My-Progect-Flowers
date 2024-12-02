from django.contrib import admin  # Добавьте эту строку
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render

# Представление для главной страницы
def home(request):
    return render(request, 'home.html')

urlpatterns = [
    path('admin/', admin.site.urls),  # Здесь используется admin, поэтому нужен импорт
    path('users/', include('users.urls')),
    path('catalog/', include('catalog.urls')),
    path('orders/', include('orders.urls')),
    path('reviews/', include('reviews.urls')),
    path('analytics/', include('analytics.urls')),
    path('', home, name='home'),  # Главная страница
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


