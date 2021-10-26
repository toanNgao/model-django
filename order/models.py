from django.db import models
from user.models import CustomerUser
from cart.models import Cart


# Create your models here.
class Order(models.Model):
    fullname = models.CharField(max_length=100, null=False)
    phone_number = models.CharField(max_length=10, null=False)
    shipping_address = models.CharField(max_length=255, null=False)
    status = models.BooleanField(default=False)
    payments = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    customer_user = models.ForeignKey(CustomerUser, on_delete=models.SET_NULL, null=True)
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)

    # total price

