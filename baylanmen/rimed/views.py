from rest_framework.viewsets import ReadOnlyModelViewSet
 
from rimed.models import Rimed
from rimed.serializer import RimedSerializer
 
class RimedViewset(ReadOnlyModelViewSet):
 
    serializer_class = RimedSerializer
 
    def get_queryset(self):
        return Rimed.objects.all()