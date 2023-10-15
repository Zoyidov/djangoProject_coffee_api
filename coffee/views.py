from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from coffee.models import Coffee
from coffee.serializers import CoffeeSerializer


class CoffeeViewSet(viewsets.ModelViewSet):
    queryset = Coffee.objects.all()
    serializer_class = CoffeeSerializer
