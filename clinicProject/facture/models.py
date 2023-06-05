from django.db import models
from django.contrib.auth.models import User
from case.models import case



# Create your models here.

class actes(models.Model):
	acte_name = models.CharField(max_length=50)
	sell_price = models.IntegerField()
	description = models.CharField(max_length=100)

	def __str__(self):
		return self.acte_name

class stock(models.Model):
	acte = models.ForeignKey(actes, on_delete=models.CASCADE, related_name='stock_acte')
	quantite = models.IntegerField()
	
	

	def __str__(self):
		return self.acte.acte_name


class facture(models.Model):
	case = models.ForeignKey(case, on_delete=models.CASCADE, related_name='facture_case')
	ammount = models.IntegerField()
	acte = models.ForeignKey(actes, on_delete=models.CASCADE, related_name='facture_acte')
	quantite = models.IntegerField()
	facture_date = models.DateField()
	facture_details = models.CharField(max_length=200)
	is_paid = models.BooleanField(default=False)

	def __str__(self):
		return self.case.patient.username




