from django.db import models
from django.db.models import Model

class player(models.Model):
    player_ID= models.CharField(max_length=200, null=False)
    player_image=models.ImageField(upload_to='images')
    player_name = models.CharField(max_length=200, null=False)
    player_age = models.IntegerField(null=False)
    player_emailID = models.CharField(max_length=200, null=False)
    player_position = models.CharField(max_length=200, null=False)
    player_height = models.CharField(max_length=200, null=False)
    player_gaurdianName = models.CharField(max_length=200, null=False)
    player_jerseyNum = models.IntegerField(max_length=200, null=False)
    player_mobileNum= models.CharField(max_length=200, null=False)
    player_addressLine1 = models.CharField(max_length=200, null=False)
    player_addressLine2 = models.CharField(max_length=200, null=False)
    player_addressLine3 = models.CharField(max_length=200, null=False)
class coach(models.Model):
    coach_ID= models.CharField(max_length=200, null=False)
    coach_image=models.ImageField(upload_to='images')
    coach_name = models.CharField(max_length=200, null=False)
    coach_age = models.IntegerField(null=False)
    coach_emailID = models.CharField(max_length=200, null=False)
    coach_mobileNum= models.CharField(max_length=200, null=False)
    coach_addressLine1 = models.CharField(max_length=200, null=False)
    coach_addressLine2 = models.CharField(max_length=200, null=False)
    coach_addressLine3 = models.CharField(max_length=200, null=False)
class team(models.Model):
    team_ID= models.CharField(max_length=200, null=False)
    team_image=models.ImageField(upload_to='images')
    team_name = models.CharField(max_length=200, null=False)

