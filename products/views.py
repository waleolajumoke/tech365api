from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializer import ProductSerializer
from .models import Product
import requests

# Create your views here.

@api_view(['GET'])
def home(request):
    products = Product.objects.all()
    products = ProductSerializer(products, many=True)
    return Response(products.data)

def index(request):
    data = requests.get('http://localhost:8000/api/v1/all-products')
    info    = data.json()
    return render(request, 'home.html', {'info': info})