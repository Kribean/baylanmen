from rest_framework.serializers import ModelSerializer
 
from fruit.models import Fruit
 
class FruitSerializer(ModelSerializer):
 
    class Meta:
        model = Fruit
        fields = '__all__'