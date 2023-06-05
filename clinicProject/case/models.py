from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class case(models.Model):
	patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='case_patient')
	secretaire = models.ForeignKey(User, on_delete=models.CASCADE, related_name='case_secretaire')
	description = models.CharField("consultation",max_length=500, default=None)
	filed_date = models.DateField()
	closed_date = models.DateField(default=None, null=True)

	def __str__(self):
		return self.patient.username + ' having ' + self.description
