from django.contrib import admin
from apps.galeria.models import Fotografia


class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "data_fotografia", "publicada")  # Fields to display
    list_display_links = ("id","nome")  # Add link to edit item on that field 
    search_fields = ('nome',)  # has to be a tuple for search
    list_filter = ("categoria","usuario") # has to be a tuple for filtering
    list_editable = ("publicada",) #  Edit at table view
    list_per_page = 10
    

admin.site.register(Fotografia, ListandoFotografias)  # import Model and adminModel

