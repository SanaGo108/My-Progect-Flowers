from django.db import models
from django.db.models import Sum, F
from users.models import User


class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', verbose_name="Пользователь")
    products = models.ManyToManyField(
        'catalog.Product',  # Ленивый импорт
        through='OrderProduct',
        related_name='orders',
        verbose_name="Товары"
    )
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default='Pending', verbose_name="Статус"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00, verbose_name="Общая сумма"
    )

    def calculate_total_price(self):
        """
        Рассчитывает общую сумму заказа на основе продуктов.
        """
        total = self.order_products.aggregate(
            total=Sum(F('quantity') * F('product__price'))
        )['total'] or 0
        self.total_price = total
        self.save()

    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ['-created_at']


class OrderProduct(models.Model):
    """
    Промежуточная модель для связи заказа и продукта,
    с учетом количества продуктов в заказе.
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_products')
    product = models.ForeignKey(
        'catalog.Product', on_delete=models.CASCADE, related_name='order_products'
    )  # Ленивый импорт
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")

    def __str__(self):
        return f"{self.quantity} x {self.product.name} for Order #{self.order.id}"

    class Meta:
        verbose_name = "Продукт заказа"
        verbose_name_plural = "Продукты заказа"


class Cart(models.Model):
    """
    Модель корзины для пользователя.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    @property
    def items(self):
        return self.cart_items.all()

    def __str__(self):
        return f"Cart for {self.user.username}"


class CartItem(models.Model):
    """
    Модель товара в корзине.
    """
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items', verbose_name="Корзина")
    product = models.ForeignKey(
        'catalog.Product', on_delete=models.CASCADE, verbose_name="Продукт"
    )  # Ленивый импорт
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    class Meta:
        verbose_name = "Товар в корзине"
        verbose_name_plural = "Товары в корзине"
