from django.contrib import admin

from fruit.models import Fruit
#from import_export import ImportExportModelAdmin


class FruitAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('nom_scientifique', 'nom_vernaculaire', 'famille_botanique', 'periode_de_fructification')


admin.site.register(Fruit,FruitAdmin) # nous modifions cette ligne, en ajoutant un deuxième argument