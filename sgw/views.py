from django.shortcuts import render
from django.http import HttpResponse

from .models import Location

# Create your views here.
def index(request):
    context = { 
        "locations": Location.objects.all()
    }
    return render(request, "sgw/index.html", context)

def home(request): 
    return HttpResponse("home")