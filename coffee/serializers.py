from rest_framework import serializers
from coffee.models import Coffee

class CoffeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coffee
        fields = ('id', 'name', 'price', 'image', 'description')