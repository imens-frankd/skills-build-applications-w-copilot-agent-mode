from django.db import models
from django.contrib.auth.models import AbstractUser
from bson import ObjectId

class Team(models.Model):
    id = models.CharField(primary_key=True, max_length=24, default=lambda: str(ObjectId()), editable=False)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class User(AbstractUser):
    id = models.CharField(primary_key=True, max_length=24, default=lambda: str(ObjectId()), editable=False)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, to_field='id', on_delete=models.SET_NULL, null=True, blank=True)

class Activity(models.Model):
    id = models.CharField(primary_key=True, max_length=24, default=lambda: str(ObjectId()), editable=False)
    user = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()  # in minutes
    distance = models.FloatField()    # in km
    timestamp = models.DateTimeField(auto_now_add=True)

class Workout(models.Model):
    id = models.CharField(primary_key=True, max_length=24, default=lambda: str(ObjectId()), editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()

class Leaderboard(models.Model):
    id = models.CharField(primary_key=True, max_length=24, default=lambda: str(ObjectId()), editable=False)
    user = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)
    points = models.IntegerField()
