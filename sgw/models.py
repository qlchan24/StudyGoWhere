from django.db import models
from django import forms

# Create your models here.
BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))


class StudySpot(models.Model):
    description = models.CharField(max_length=100)

    crowdednessRating = models.IntegerField()
    airConditioned = models.BooleanField(choices=BOOL_CHOICES, blank=False, null=True, default=None)
    discussionFriendly = models.BooleanField(choices=BOOL_CHOICES, blank=False, null=True, default=None)
    wallSockets = models.BooleanField(choices=BOOL_CHOICES, blank=False, null=True, default=None)

    levelNumber = models.IntegerField()
    locationName = models.CharField(max_length=100)
    openingTime = models.IntegerField()  # need to change to timefield
    closingTime = models.IntegerField()  # need to change to timefield

    def __str__(self):
        return f"{self.locationName} > Level {self.levelNumber} > {self.description}"
    
