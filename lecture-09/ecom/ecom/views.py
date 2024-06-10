from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView
from ecom.models import Product
from ecom.serializer import ProductSerializer
from rest_framework.permissions import IsAuthenticated


class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]