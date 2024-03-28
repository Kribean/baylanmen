from django.contrib import admin

from rimed.models import Rimed
from import_export.admin import ImportExportModelAdmin


class RimedAdmin(ImportExportModelAdmin,admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('scientific_name', 'vernacular_names', 'botanical_family')


admin.site.register(Rimed,RimedAdmin) # nous modifions cette ligne, en ajoutant un deuxième argument