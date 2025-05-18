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
