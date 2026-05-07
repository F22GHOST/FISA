from django.db import models
from django.contrib.auth.models import User

class Division(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Rank(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField()

    def __str__(self):
        return self.name

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roblox_username = models.CharField(max_length=100)
    discord_username = models.CharField(max_length=100)
    roleplay_name = models.CharField(max_length=100)
    callsign = models.CharField(max_length=20)
    rank = models.ForeignKey(Rank, on_delete=models.SET_NULL, null=True)
    divisions = models.ManyToManyField(Division, blank=True)
    personal_file = models.TextField(blank=True)
    is_hrt = models.BooleanField(default=False)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.roleplay_name