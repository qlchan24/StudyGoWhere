from django.urls import path
from sgw import views

app_name = 'sgw'
urlpatterns = [
    path("", views.home, name="home"),
    path("locations", views.index, name="list-of-locations"),
]
