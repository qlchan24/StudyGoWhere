from django import forms
from django.forms import ModelForm
from django.db import models
from .models import StudySpot, Rating, Location, StudySpotContrib


class ContributeStudySpotForm(forms.ModelForm):
    class Meta:
        model = StudySpot
        fields = '__all__'
        widgets = {'airConditioned': forms.RadioSelect,
                   'discussionFriendly': forms.RadioSelect,
                   'wallSockets': forms.RadioSelect
                   }

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


class ContributeRatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = '__all__'

    # crowdednessRating = models.IntegerField()
    # timeOfRating = models.DateTimeField()       # doesnt really work for now


class ContributeLocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'


class StudySpotContribForm(forms.ModelForm):
    class Meta:
        model = StudySpotContrib
        fields = '__all__'  # user and geom to be manipulated before saving to form
        widgets = {'airConditioned': forms.RadioSelect,
                   'discussionFriendly': forms.RadioSelect,
                   'wallSockets': forms.RadioSelect
                   }
        labels = {
            "studyspotname": "Name of the place",
            "levelNumber": "Level number",
            "openingTime": "Opening time (skip if unsure or not applicable)",
            "closingTime": "Closing time (skip if unsure or not applicable)",
            "airConditioned": "Is the place Air-Conditioned",
            "discussionFriendly": "Is the place discussion friendly",
            "wallSockets": "Are there wall sockets that can be used",
            "image": "Please upload a square image of the place",
        }
