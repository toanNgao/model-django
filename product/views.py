from django.shortcuts import render
from rest_framework import viewsets
from .models import Product, Image, Category
from .serializers import ProductSerializer, ImageSerializer, CategorySerializer


# Create your views here.
class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.filter(active=True)
    serializer_class = ImageSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(active=True)
    serializer_class = ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter()
    serializer_class = CategorySerializer
