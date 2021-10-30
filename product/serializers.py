from rest_framework.serializers import ModelSerializer
from .models import Product, Image, Category


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'created_at', 'category', 'brand', 'thumbnail']


class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image', 'product']


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'description']
