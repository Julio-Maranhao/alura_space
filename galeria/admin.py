from django.contrib import admin
from galeria.models import Fotografia


class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda")  # Fields to display
    list_display_links = ("id","nome")  # Add link to edit item on that field 
    search_fields = ('nome',)  # has to be a tuple for search
    

admin.site.register(Fotografia, ListandoFotografias)  # import Model and adminModel

