from django.db import models


class Product(models.Model):
    objects = None
    name = models.CharField(max_length=200)
    description = models.TextField(default="Описание отсутствует")  # Значение по умолчанию
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')  # Загружаются в папку media/products/

    def __str__(self):
        return self.name
