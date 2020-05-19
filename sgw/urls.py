from django.urls import path
from . import views

app_name = 'sgw'
urlpatterns = [
    path("", views.home, name="home"),
    path("locations/", views.index, name="list-of-locations"),
    path("locations/<str:location>/", views.locationpage, name="locationpage"),
    path("locations/<str:location>/<str:studyspot>", views.studyspotpage, name="studyspotpage"), # to be changed
    path("studyspot-contribution/", views.contributeStudySpot,
         name="studyspot-contribution-page"),
    path("rating-contribution/", views.contributeRating,
         name="rating-contribution-page"),
]
