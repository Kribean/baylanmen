from rest_framework.serializers import ModelSerializer
 
from rimed.models import Rimed
 
class RimedSerializer(ModelSerializer):
 
    class Meta:
        model = Rimed
        fields = '__all__'