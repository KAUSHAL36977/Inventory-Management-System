# settings.py
INSTALLED_APPS = [
    ...
    'rest_framework',
    'api',
]

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',  # Default JSON responses
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    ),
}

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'inventory',
        'ENFORCE_SCHEMA': True,
        'CLIENT': {
            'host': 'your_mongo_host',  # Add your MongoDB connection URL
            'username': 'your_username',
            'password': 'your_password',
            'authSource': 'admin',
        }
    }
}
















# api/models.py
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator

class Supplier(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(
        max_length=15,
        validators=[RegexValidator(r'^\+?1?\d{9,15}$')],
        unique=True
    )
    address = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    stock = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    supplier = models.ForeignKey(Supplier, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]

    product = models.ForeignKey(Product, related_name='orders', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.product.name}"















# api/serializers.py
from rest_framework import serializers
from .models import Product, Supplier, Order

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'

    def validate(self, data):
        product = data['product']
        quantity = data['quantity']
        if product.stock < quantity:
            raise serializers.ValidationError(f"Not enough stock for {product.name}. Available: {product.stock}")
        data['total_price'] = product.price * quantity
        return data














# api/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Product, Supplier, Order
from .serializers import ProductSerializer, SupplierSerializer, OrderSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.prefetch_related('orders').all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.select_related('product').all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        order = serializer.save()
        product = order.product
        product.stock -= order.quantity
        product.save()













# api/tests.py
from django.test import TestCase
from .models import Supplier, Product, Order

class SupplierTestCase(TestCase):
    def setUp(self):
        self.supplier = Supplier.objects.create(
            name="Test Supplier",
            email="supplier@example.com",
            phone="+1234567890",
            address="123 Test St"
        )

    def test_supplier_creation(self):
        self.assertEqual(Supplier.objects.count(), 1)
        self.assertEqual(self.supplier.name, "Test Supplier")

