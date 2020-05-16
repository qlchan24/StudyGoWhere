from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .models import StudySpot
from .forms import ContributeStudySpotForm

# Create your views here.


def index(request):
    context = {
        "locations": StudySpot.objects.order_by().values('locationName').distinct()
    }
    return render(request, "sgw/index.html", context)


def home(request):
    return HttpResponse("home")


def locationpage(request, location):
    locationquery = StudySpot.objects.filter(locationName=location)
    context = {
        "location": location,
        "openingTime": locationquery.first.openingTime,
        "closingTime": locationquery.first.closingTime,
        "levelNumber": locationquery.order_by().values('levelNumber').distinct()
    }
    return render(request, "sgw/locationpage.html", context)


def contributeStudySpot(request):
    if request.method == 'POST':
        form = ContributeStudySpotForm(request.POST)
        if form.is_valid():
            return HttpResponse('alright')  # not sure about this?
    else:
        form = ContributeStudySpotForm()

    return render(request, 'contributeStudySpot.html', {'form': form})
