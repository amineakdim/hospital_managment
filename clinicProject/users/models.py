from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Doctor(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	contact_no = models.IntegerField()
	speciality = models.CharField(max_length=100)
	sex = models.CharField(max_length=1)
	CIN = models.CharField(max_length=7)
	
	def __str__(self):
		return self.user.username


class Secretaire(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_no = models.IntegerField(default=True)
    sex = models.CharField(max_length=1)
    CIN = models.CharField(max_length=7)

    def __str__(self):
    	return self.user.username
		