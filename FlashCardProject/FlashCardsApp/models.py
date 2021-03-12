from django.db import models
from django.contrib.auth.models import User

class Card(models.Model):
    word = models.CharField(max_length=100)
    definition = models.TextField()
    lastShowed = models.DateTimeField()
    showAt = models.DateTimeField()
    wordBin = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    incorrect = models.IntegerField(default=0)
