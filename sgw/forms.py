from django import forms
from django.db import models
from .models import StudySpot

class ContributeStudySpotForm(forms.Form): 
    description = forms.CharField(max_length=100)
    class Meta:
        model = StudySpot
        widgets = {
            'airConditioned': forms.RadioSelect, 
            'discussionFriendly': forms.RadioSelect,
            'wallSockets': forms.RadioSelect,
        }
    levelNumber = models.IntegerField()
    locationName = models.CharField(max_length=100)
    crowdednessRating = models.IntegerField()

    closingTime = models.IntegerField()
    