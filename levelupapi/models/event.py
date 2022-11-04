from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):

    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name='event_game')
    description = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    organizer = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name='event_organizer')
    gamers = models.ManyToManyField("Gamer")