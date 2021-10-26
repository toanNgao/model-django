from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=False)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    description = models.TextField(default='')


class Brand(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=False, unique=True)
    phone_number = models.CharField(max_length=10, default='')
    address = models.CharField(max_length=255, default='')
    logo = models.ImageField(upload_to='brand/%Y/%m')


class Product(models.Model):
    name = models.CharField(max_length=100, null=False)
    slug = models.SlugField(max_length=100, default='')
    description = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)

    class Meta:
        unique_together = ('name', 'category')


class Image(models.Model):
    image = models.ImageField(upload_to='product/%Y/%m')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)


class ProductVariation(models.Model):
    size = models.IntegerField(default=0)
    color = models.CharField(max_length=50, default='')
    price = models.IntegerField(default=0)
    sale_price = models.IntegerField(blank=True, null=True)
    inventory_quantity = models.IntegerField(default=0)
    sold = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)


class Interact(models.Model):
    vote = models.BooleanField(blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # user


class Comment(models.Model):
    content = models.TextField(default='')
    interact = models.ForeignKey(Interact, on_delete=models.CASCADE)
    cm = models.ForeignKey('self', on_delete=models.CASCADE)