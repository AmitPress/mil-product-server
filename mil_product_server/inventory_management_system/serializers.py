from rest_framework import serializers
from .models import Product, Stock, Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['created_at', 'updated_at', 'id']

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        exclude = ['created_at', 'updated_at', 'id']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ['created_at', 'updated_at', 'id']