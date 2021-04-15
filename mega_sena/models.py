from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    numbers = models.TextField()
    date = models.DateField(auto_now=True)
    user = models.ForeignKey(User, models.CASCADE)
