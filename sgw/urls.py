from django.urls import path, re_path
from . import views
from .models import Location
from djgeojson.views import GeoJSONLayerView

app_name = 'sgw'
urlpatterns = [
    path("", views.home, name="home"),
    path("locations/", views.index, name="list-of-locations"),
    path("locations/<str:location>/", views.locationpage, name="locationpage"),
    path("locations/<str:location>/<str:studyspot>",
         views.studyspotpage, name="studyspotpage"),  # to be changed
    path("studyspot-contribution/", views.contributeStudySpot,
         name="studyspot-contribution-page"),
    path("rating-contribution/", views.contributeRating,
         name="rating-contribution-page"),
    path("location-contribution/", views.contributeLocation,
         name="location-contribution-page"),
    path("map/", views.mapview, name="map"),
    re_path(r'^data.geojson$', GeoJSONLayerView.as_view(model=Location,
                                                        properties=('locationName', 'geom', 'openingTime')), name="data"),
]
