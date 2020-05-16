from django.db import models

# Create your models here.

class StudySpot(models.Model): 
    crowdednessRating = models.IntegerField()
    airConditioned = True
    discussionFriendly = True
    wallSockets = True

    levelNumber = models.IntegerField()
    locationName = models.CharField(max_length=100)

    closingTime = models.IntegerField()



    



