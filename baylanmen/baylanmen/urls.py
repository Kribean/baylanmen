from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
 
from fruit.views import FruitViewset
from rimed.views import RimedViewset
 
# Ici nous créons notre routeur
router = routers.SimpleRouter()

router.register('fruit', FruitViewset, basename='fruit')
router.register('rimed', RimedViewset, basename='rimed')
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls))
]