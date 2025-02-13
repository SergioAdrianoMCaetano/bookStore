from django.urls import path, include
from rest_framework import routers

from product import viewset

router = routers.SimpleRouter()
router.register(r'product', viewset.ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
]

