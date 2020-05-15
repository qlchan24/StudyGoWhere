from django.db import models

# Create your models here.


class Level(models.Model):
    number = models.IntegerField()
    crowdedness = models.IntegerField()
    airConditioned = True
    discussionFriendly = True
    wallSockets = True


class Location(models.Model):
    name = models.CharField(max_length=100)
    levels = models.ForeignKey(Level, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

