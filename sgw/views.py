from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .models import StudySpot, Rating
from .forms import ContributeStudySpotForm, ContributeRatingForm
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
        "levelNumber": list(locationquery.order_by().values_list('levelNumber', flat=True).distinct()),
        "description": list(locationquery.order_by().values_list('description', flat=True).distinct())
    }
    return render(request, "sgw/locationpage.html", context)

def studyspotpage(request, studyspot): 
    studyspotquery = StudySpot.objects.filter(description=studyspot)
    context = { 
        "studyspot": studyspot,
         "ratings": list(Rating.objects.filter(studyspot=studyspot))
    }
    return render(request, "sgw/studyspotpage.html", context)

def contributeStudySpot(request):
    if request.method == 'POST':
        form = ContributeStudySpotForm(request.POST)
        if form.is_valid():
            studyspot = form.save()
            return HttpResponseRedirect(reverse('sgw:list-of-locations'))
            # return render(request, 'sgw/index.html', {'studyspots':studyspots})  # not sure about this?
    else:
        form = ContributeStudySpotForm()
    return render(request, 'contributeStudySpot.html', {'form': form})

def contributeRating(request):
    if request.method == 'POST':
        form = ContributeRatingForm(request.POST)
        if form.is_valid():
            rating = form.save()
            return HttpResponseRedirect(reverse('sgw:list-of-locations'))
    else:
        form = ContributeRatingForm()

    return render(request, 'contributeRating.html', {'form': form, "studyspots": list(StudySpot.objects.all())})