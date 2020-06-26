from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404

from .models import StudySpot, Rating, Location
from .forms import *
from django.urls import reverse

from django.contrib import messages

from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder

# from .serializers import RatingSerializer, LocationSerializer, StudySpotSerializer

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
    # loc = Location.objects.get(locationName=location)
    context = {
        "location": loc,
        "openingTime": loc.openingTime,
        "closingTime": loc.closingTime,
        "levelNumber": list(StudySpot.objects.filter(locationName=loc).values_list('levelNumber', flat=True).distinct()),
        "description": list(StudySpot.objects.filter(locationName=loc))
    }
    return render(request, "sgw/locationpage.html", context)


def studyspotpage(request, location, studyspot):
    studyspotquery = get_object_or_404(StudySpot, description=studyspot)
    context = {
        "studyspot": studyspot,
        "ratings": list(Rating.objects.filter(studyspot=studyspotquery)),
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

# Obsolete


def contributeLocation(request):
    if request.method == 'POST':
        form = ContributeLocationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['locationName']
            if Location.objects.filter(locationName=name).exists():
                messages.error(request, "fdkfdhlkfeh")  # error not showing
                # return HttpResponseRedirect(reverse('sgw:location-contribution-page'))
            else:
                location = form.save()
                return HttpResponseRedirect(reverse('sgw:list-of-locations'))
    else:
        form = ContributeLocationForm()
    return render(request, 'contributeLocation.html', {'form': form})


def mapview(request):
    form = StudySpotContribForm()

    context = {
        "locations": list(Location.objects.all()),
        "studyspots": list(StudySpot.objects.all()),
        "ratings": list(Rating.objects.all()),
        "form": form
    }
    return render(request, "sgw/leaflet.html", context)


def locationjson(request):
    data = serializers.serialize(
        "json", Location.objects.all(), cls=DjangoJSONEncoder)
    return HttpResponse(data, content_type="application/JSON")


def studyspotjson(request):
    data = serializers.serialize(
        "json", StudySpot.objects.all(), cls=DjangoJSONEncoder)
    return HttpResponse(data, content_type="application/JSON")


def ratingjson(request):
    data = serializers.serialize(
        "json", Rating.objects.all(), cls=DjangoJSONEncoder)
    return HttpResponse(data, content_type="application/JSON")


def ratingform(request):
    if request.method == 'POST':
        value = request.POST['value']
        ssname = request.POST['ssname']

        print("creating new rating: "+value)

        Rating.objects.create(
            crowdedness=value,
            studyspot=StudySpot.objects.get(description=ssname)
        )
        print(Rating.objects.all)
    return HttpResponse('')


def contributeStudySpotForm(request):
    if request.method == 'POST':
        dic = request.POST.dict()
        print(dic)
        dic['geom'] = {'type': "Point",
                       'coordinates': list(map(float, request.POST['geom'].split(',')))}
        form = StudySpotContribForm(dic, request.FILES)
        print("posted")
        if form.is_valid():
            studySpotContrib = form.save()
            print("saved")
        else:
            print(form.errors)
    return HttpResponse('')
