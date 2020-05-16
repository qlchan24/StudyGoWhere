from django.shortcuts import render
from django.http import HttpResponse

from .models import StudySpot

# Create your views here.
def index(request):
    context = { 
        "studyspots": StudySpot.objects.all()
    }
    return render(request, "sgw/index.html", context)

def home(request): 
    return HttpResponse("home")

#def contribution(request): 
#    return 