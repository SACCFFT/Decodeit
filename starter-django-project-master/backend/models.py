from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.



class Player(models.Model):
	user = models.OneToOneField(User, related_name="member", default='')
	name = models.CharField(max_length=200, default="")
	username = models.CharField(max_length=40, default="", primary_key=True)
	score = models.IntegerField(default=0)
	key = models.CharField(max_length=26, default="")
	plainText = models.CharField(max_length=1000, default="")
	cipherText = models.CharField(max_length=1000, default="")


