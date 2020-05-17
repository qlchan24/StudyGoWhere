from django import forms
from django.forms import ModelForm
from django.db import models
from .models import StudySpot

class ContributeStudySpotForm(ModelForm): 
    class Meta: 
        model = StudySpot
        fields = ['description','crowdednessRating','airConditioned','discussionFriendly',
        'wallSockets','levelNumber','locationName','openingTime','closingTime']

    # description = forms.CharField(max_length=100)
    # class Meta:
    #     model = StudySpot
    #     widgets = {
    #         'airConditioned': forms.RadioSelect, 
    #         'discussionFriendly': forms.RadioSelect,
    #         'wallSockets': forms.RadioSelect,
    #     }
    # levelNumber = models.IntegerField()
    # locationName = models.CharField(max_length=100)
    # crowdednessRating = models.IntegerField()

    # closingTime = models.IntegerField()
    