from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView
from ecom.models import Product
from ecom.serializer import ProductSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class EmptyException(Exception):
    pass

class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

class ProductAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        if len(products) == 0:
            raise EmptyException()

        return ProductSerializer(products, many=True)