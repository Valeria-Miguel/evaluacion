from rest_framework import serializers
from .models import Flower

class FlowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flower
        fields = ['id', 'name', 'price', 'stock', 'description', 'created_at', 'updated_at']
from rest_framework import serializers
from .models import Flower

class FlowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flower
        fields = '__all__'
