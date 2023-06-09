from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_no = models.IntegerField()
    address = models.CharField(max_length=200)
    dob = models.DateField()
    blood_group = models.CharField(max_length=3)
    sex = models.CharField(max_length=1)
    CIN = models.CharField(max_length=10,default=True)
    profession = models.CharField(max_length=100,default=True)

    def __str__(self):
        return self.user.username


