from django.contrib import admin
from .models import Gemeinde, Leistungsanbietende

class GemeindeAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Hier können Sie weitere Feldnamen hinzufügen

class LeistungsanbietendeAdmin(admin.ModelAdmin):
    list_display = ('name', 'taetigkeit', 'beschreibung', 'leistung', 'internetlink')
    filter_horizontal = ('gemeinde',)  # Für ManyToMany-Felder

admin.site.register(Gemeinde, GemeindeAdmin)
admin.site.register(Leistungsanbietende, LeistungsanbietendeAdmin)
