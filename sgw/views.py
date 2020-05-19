from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .models import StudySpot
from .forms import ContributeStudySpotForm
from django.urls import reverse

# Create your views here.


def index(request):
    context = {
        "locations": list(StudySpot.objects.order_by().values_list('locationName', flat=True).distinct())
    }
    return render(request, "sgw/index.html", context)


def home(request):
    return HttpResponse("home")


def locationpage(request, location):
    locationquery = StudySpot.objects.filter(locationName=location)
    context = {
        "location": location,
        "openingTime": list(locationquery.values_list('openingTime', flat=True))[0],
        "closingTime": list(locationquery.values_list('closingTime', flat=True))[0],
        "levelNumber": list(locationquery.order_by().values_list('levelNumber', flat=True).distinct())
    }
    return render(request, "sgw/locationpage.html", context)


def contributeStudySpot(request):
    if request.method == 'POST':
        form = ContributeStudySpotForm(request.POST)
        if form.is_valid():
            StudySpot = form.save()
            return HttpResponseRedirect(reverse('sgw:list-of-locations'))
    else:
        form = ContributeStudySpotForm()

    return render(request, 'contributeStudySpot.html', {'form': form})
