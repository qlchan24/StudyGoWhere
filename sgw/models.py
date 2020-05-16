from django.db import models

# Create your models here.
BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))


class StudySpot(models.Model):
    description = models.CharField(max_length=100)

    crowdednessRating = models.IntegerField()
    airConditioned = models.BooleanField(choices=BOOL_CHOICES)
    discussionFriendly = models.BooleanField(choices=BOOL_CHOICES)
    wallSockets = models.BooleanField(choices=BOOL_CHOICES)

    levelNumber = models.IntegerField()
    locationName = models.CharField(max_length=100)
    openingTime = models.IntegerField()
    closingTime = models.IntegerField()
