from rest_framework import serializers
from .models import FoodSale

class FoodSalesSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodSale
        fields = '__all__'