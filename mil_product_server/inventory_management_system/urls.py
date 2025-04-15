from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='mymodel')

urlpatterns = [
    path(r'', include(router.urls), name="api")
]