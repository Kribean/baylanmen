from rest_framework.viewsets import ReadOnlyModelViewSet
 
from fruit.models import Fruit
from fruit.serializer import FruitSerializer
 
class FruitViewset(ReadOnlyModelViewSet):
 
    serializer_class = FruitSerializer
 
    def get_queryset(self):
        return Fruit.objects.all()