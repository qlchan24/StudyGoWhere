from django.shortcuts import render
from django.http import HttpResponse

from .models import StudySpot

# Create your views here.


def index(request):
    context = {
        "locations": StudySpot.objects.order_by().values('locationName').distinct()
    }
    return render(request, "sgw/index.html", context)


def home(request):
    return HttpResponse("home")

# def contribution(request):
#    return


def locationpage(request, location):
    locationquery = StudySpot.objects.filter(locationName=location)
    context = {
        "location": location,
        "openingTime": locationquery.first.openingTime,
        "closingTime": locationquery.first.closingTime,
        "levelNumber": locationquery.order_by().values('levelNumber').distinct()
    }
    return render(request, "sgw/locationpage.html", context)
