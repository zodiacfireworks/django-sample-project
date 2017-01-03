from django.contrib import admin

from .models import Neighborhood
from .models import Property



@admin.register(Neighborhood)
class NeighborhoodAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'address'
    ]


class PropertyAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'neighborhood'
    ]


admin.site.register(Property, PropertyAdmin)
