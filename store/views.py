from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.request.method in ["POST", "PUT", "DELETE"]:
            return [IsAdminUser()]
        return [AllowAny()]
