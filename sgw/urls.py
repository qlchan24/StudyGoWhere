from django.urls import path
from . import views

app_name = 'sgw'
urlpatterns = [
    path("", views.home, name="home"),
    path("locations", views.index, name="list-of-locations"),
    # path("studyspot-contribution", views.contribution, name = "studyspot-contribution-page")
    path("locations/<str:location>", views.locationpage, name="locationpage"),
]
