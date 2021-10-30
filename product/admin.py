from django.contrib import admin
from django.utils.html import mark_safe
from .models import *


class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'product']
    readonly_fields = ['avatar']

    def avatar(self, image):
        return mark_safe('<img src="http://127.0.0.1:8000/{img_url}" alt="{alt}" style="width: 200px" /img>'.format(img_url=image.image, alt=image.product))


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at', 'active', 'category', 'brand']
    search_fields = ['name', 'category__name']
    ordering = ['-id']
    readonly_fields = ['avatar']

    def avatar(self, thumbnail):
        return mark_safe('<img src="http://127.0.0.1:8000/{img_url}" alt="{alt}" style="width: 200px" /img>'.format(img_url=thumbnail.thumbnail, alt=thumbnail.name))


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(ProductVariation)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Interact)
admin.site.register(Comment)
