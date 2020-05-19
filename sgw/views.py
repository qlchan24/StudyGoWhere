from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import StudySpot, Rating, Location
from .forms import ContributeStudySpotForm, ContributeRatingForm
from django.urls import reverse

# Create your views here.


def index(request):
    context = {
        "locations": list(Location.objects.all())
    }
    return render(request, "sgw/index.html", context)


def home(request):
    return HttpResponse("home")


def locationpage(request, location):
    loc = get_object_or_404(Location, locationName=location)
    context = {
        "location": loc,
        "openingTime": loc.openingTime,
        "closingTime": loc.closingTime,
        "levelNumber": list(StudySpot.objects.filter(Location=loc).values_list('levelNumber', flat=True).distinct()),
        "description": list(StudySpot.objects.filter(Location=loc))
    }
    return render(request, "sgw/locationpage.html", context)


def studyspotpage(request, location, studyspot):
    studyspotquery = StudySpot.objects.filter(description=studyspot)
    context = {
        "studyspot": studyspot,
        "ratings": list(Rating.objects.filter(studyspot=studyspotquery.first())),
        "location": location,
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
