from django.db import models

# Create your models here.
class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    class Meta:
        abstract = True

class Product(BaseModel):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=256)
    origin = models.CharField(50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey("Category", null=True, on_delete=models.SET_NULL)
    stock = models.ForeignKey("Stock", on_delete=models.DO_NOTHING)
    class Meta:
        db_table = "products"


class Stock(BaseModel):
    STATUS_CHOICES = (
        ("available", "Available"),
        ("out", "Out"),
    )
    session = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="available")
    discout = models.DecimalField(max_digits=2, decimal_places=2)
    class Meta:
        db_table = "stocks"


class Category(BaseModel):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=256)
    base_price = models.DecimalField(max_digits=6, decimal_places=2) # uptil $9999.99
    discount = models.DecimalField(max_digits=2, decimal_places=2) # will represent percentage
    class Meta:
        db_table = "categories"