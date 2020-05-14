from django.urls import path
from sgw import views

urlpatterns = [
    path("", views.home, name="home"),
]
