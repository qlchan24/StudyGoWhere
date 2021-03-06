from django.urls import path, re_path
from . import views
from .models import Location, StudySpot, Rating
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
    path("location.json", views.locationjson, name="locationjson"),
    path("rating.json", views.ratingjson, name="ratingjson"),
    path("studyspot.json", views.studyspotjson, name="studyspotjson"),
    path("ratingform", views.ratingform, name="ratingform"),
    path("studyspotcontrib", views.contributeStudySpotForm, name="studyspotform"),
    path("login", views.login_view, name="loginform"),
    path("logout", views.logout_view, name="logout"),
    path("usercreation", views.usercreate, name="usercreation"),
    path("complaint", views.complaintview, name="complaint"),
    path('addtofavorites', views.addtofavorites, name="addtofavorites"),
    path("favjson", views.favoritesjson, name="favjson"),
    re_path(r'^data.geojson$', GeoJSONLayerView.as_view(model=Location,
                                                        properties=('locationName', 'geom', 'openingTime', 'closingTime')), name="data"),
]
