from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('product', views.ProductViewSet)
router.register('image', views.ImageViewSet)
router.register('category', views.CategoryViewSet)


urlpatterns = [
    path('', include(router.urls)),
]