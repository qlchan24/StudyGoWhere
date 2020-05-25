from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Location, StudySpot, Rating


# Register your models here.
admin.site.register(Location, LeafletGeoAdmin)
admin.site.register(StudySpot)
admin.site.register(Rating)
