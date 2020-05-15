from django.db import models

# Create your models here.
class Level(models.Model): 
    number = models.IntegerField(max_length = 2)
    crowdedness = models.IntegerField(max_length=3)
    airConditioned = True
    discussionFriendly = True
    wallSockets = True
    
class Location(models.Model): 
    name = models.CharField()
    levels = models.ForeignKey(Level, on_delete=models.CASCADE)

    def __str__(self): 
        return f"{self.name}"



