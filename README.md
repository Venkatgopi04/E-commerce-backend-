# E-commerce-backend-
Step 1: Install Django
pip install django==3.2
Step 2: Create Django Project
django-admin startproject ECommerceBackend
Step 3: Setup MySQL with XAMPP
Open XAMPP → Start Apache & MySQL
Visit: http://localhost/phpmyadmin
Create a database named: ecommerce_db
Step 4: Create Virtual Environment
python -m venv Env
cd Env/Scripts
activate
cd ../..
Step 5: Install Django inside Virtual Environment
pip install django==3.2
Step 6: Create Django App
cd ECommerceBackend
python manage.py startapp ProductApp
Step 7: Register App in settings.py
INSTALLED_APPS = [
    ...
    'corsheaders',
    'rest_framework',
    'ProductApp.apps.ProductappConfig',
]
Step 8: Add Middleware & CORS Config
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    ...
]

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_ALL_HEADERS = True
Step 9: Define Product Model
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    available = models.BooleanField(default=True)
Step 10: Create Serializer
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
Step 11: Install Required Packages
pip install django-cors-headers
pip install djangorestframework
pip install dj-database-url
pip install pymysql
pip install mysqlclient
Step 12: Configure Database
import dj_database_url
import pymysql
pymysql.install_as_MySQLdb()

DATABASES = {
    'default': dj_database_url.parse('mysql://root@localhost/ecommerce_db')
}
Step 13: Run Migrations
python manage.py makemigrations
python manage.py migrate
Step 14: Create Views
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .models import Product
from .serializers import ProductSerializer

@csrf_exempt
def productApi(request, id=0):
    if request.method == 'GET':
        if id > 0:
            product = Product.objects.get(id=id)
            serializer = ProductSerializer(product)
            return JsonResponse(serializer.data, safe=False)
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Product Added", safe=False)
        return JsonResponse("Failed to Add", safe=False)

    elif request.method == 'DELETE':
        product = Product.objects.get(id=id)
        product.delete()
        return JsonResponse("Product Deleted", safe=False)
        Step 15: Configure URLs
        from django.contrib import admin
from django.urls import path, re_path
from ProductApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^products$', views.productApi),
    re_path(r'^products/([0-9]+)$', views.productApi),
]
API Endpoints
products


