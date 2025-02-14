from rest_framework import serializers
from .models import Flower

class FlowerSerializer(serializers.ModelSerializer):
    class Meta:
      
        model = Flower
         # de campos que seran incluidos en la serializacion
        fields = ['id', 'name', 'price', 'stock', 'description', 'created_at', 'updated_at']
from rest_framework import serializers
from .models import Flower

class FlowerSerializer(serializers.ModelSerializer):
    class Meta:   # se especifica que el modelo que se esta serializando es 'Flower'
        model = Flower
        fields = '__all__'        # todos campos que seran incluidos en la serializacion
