from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from user.permissions import IsAssistant, IsManager
from .models import Product, Stock, Category
from .serializers import ProductSerializer, StockSerializer, CategorySerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        match self.request.method:
            case 'POST' | 'PUT' | 'PATCH' | 'DELETE': return [IsAssistant(), IsManager()] # only assistant or manafer can do editing
        return [AllowAny()] # ready only for others

class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    def get_permissions(self):
        match self.request.method:
            case 'POST' : return [IsManager(), IsAssistant()] # manager and assistant can create only
            case 'PUT' | 'PATCH' | 'DELETE': return [IsManager()] # updation and deletion is manager dependent
        return [AllowAny()]

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        match self.request.method:
            case 'POST' | 'PUT' | 'PATCH' | 'DELETE': return [IsManager()] # manager is the sole hero here
        return [AllowAny()]
