from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Product)
admin.site.register(Image)
admin.site.register(ProductVariation)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Interact)
admin.site.register(Comment)

