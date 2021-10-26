from django.db import models
from product.models import ProductVariation


# Create your models here.
class Voucher(models.Model):
    code = models.CharField(max_length=25, null=False)
    rate = models.ImageField(default=0)


class Cart(models.Model):
    transport_fee = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    voucher = models.ForeignKey(Voucher, on_delete=models.CASCADE)
    # price


class CartItem(models.Model):
    quantity = models.IntegerField(default=1)
    note = models.TextField(default='', blank=True)
    # unit_price
    product_variation = models.ForeignKey(ProductVariation, on_delete=models.SET_NULL, null=True)
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)
