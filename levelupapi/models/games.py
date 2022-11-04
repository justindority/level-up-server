from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):

    game_type = models.ForeignKey("GameType", on_delete=models.CASCADE, related_name='game_type')
    title = models.CharField(max_length=50)
    maker = models.CharField(max_length=50)
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name='game_gamer')
    number_of_players = models.IntegerField(blank=False, null=False)
    skill_level = models.IntegerField(blank=False, null=False)
