from django.db import models
from django import forms
from djgeojson.fields import PointField

# Create your models here.
BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))


class Location(models.Model):
    locationName = models.CharField(max_length=100)
    openingTime = models.TimeField(default='20:00')
    closingTime = models.TimeField(default='20:00')
    geom = PointField()
    image = models.ImageField(upload_to='location')

    def __str__(self):
        return self.locationName


class StudySpot(models.Model):
    description = models.CharField(max_length=100)
    airConditioned = models.BooleanField(
        choices=BOOL_CHOICES, blank=False, null=True, default=None)
    discussionFriendly = models.BooleanField(
        choices=BOOL_CHOICES, blank=False, null=True, default=None)
    wallSockets = models.BooleanField(
        choices=BOOL_CHOICES, blank=False, null=True, default=None)
    levelNumber = models.IntegerField()
    locationName = models.ForeignKey(Location, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='studyspot')

    def __str__(self):
        return f"{self.locationName} -> Level {self.levelNumber} -> {self.description}"


class Rating(models.Model):
    crowdedness = models.IntegerField()         # need to change to slider
    studyspot = models.ForeignKey(StudySpot, on_delete=models.CASCADE)
    whenRated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.crowdedness}% ({self.whenRated})"


class StudySpotContrib(models.Model):
    user = models.CharField(max_length=100)
    openingTime = models.TimeField(default='20:00')
    closingTime = models.TimeField(default='20:00')
    image = models.ImageField(upload_to='studyspot')
    geom = PointField()
    studyspotname = models.CharField(max_length=100)
    levelNumber = models.IntegerField()
    airConditioned = models.BooleanField(
        choices=BOOL_CHOICES, blank=False, null=True, default=None)
    discussionFriendly = models.BooleanField(
        choices=BOOL_CHOICES, blank=False, null=True, default=None)
    wallSockets = models.BooleanField(
        choices=BOOL_CHOICES, blank=False, null=True, default=None)
