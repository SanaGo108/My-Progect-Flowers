from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from django.contrib.auth import views as auth_views
from users.views import dashboard
from orders.views import cart  # Импорт для прямого маршрута корзины

def home(request):
    return render(request, 'home.html', {'current_page': 'home'})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('catalog/', include('catalog.urls')),
    path('orders/', include('orders.urls')),
    path('reviews/', include('reviews.urls')),
    path('analytics/', include('analytics.urls')),
    path('dashboard/', dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('cart/', cart, name='cart'),  # Прямой маршрут для корзины
    path('', home, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
