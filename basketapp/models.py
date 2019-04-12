from django.db import models
from django.conf import settings
from mainapp.models import Product


class Basket(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='quantity', default=1)
    add_datetime = models.DateTimeField(verbose_name='time', auto_now_add=True)

    def __str__(self):
        return self.user.username + ' ' + self.product.name