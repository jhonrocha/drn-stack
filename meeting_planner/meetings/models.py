from django.db import models
from datetime import time

# Create your models here.


class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"


class Room(models.Model):
    name = models.CharField(max_length=200)
    floor = models.IntegerField(default=1)
    room = models.IntegerField(default=101)

    def __str__(self):
        return f"{self.name} at {self.fllor} on {self.room}"
