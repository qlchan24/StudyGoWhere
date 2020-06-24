from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import *


# Register your models here.
admin.site.register(Location, LeafletGeoAdmin)
admin.site.register(StudySpot)
admin.site.register(Rating)
admin.site.register(StudySpotContrib)
