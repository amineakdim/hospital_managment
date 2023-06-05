from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,Group
from .models import Patient
from django.template.context_processors import csrf
from home.context_processors import hasGroup
from django.contrib import messages



@login_required
def myProfile(request):
	c={}
	if hasGroup(request.user, 'patient'):
		c['isPatient'] = True
	return render(request, 'my_profile.html')


@login_required
def register(request):
	if hasGroup(request.user, 'secretaire'):
		c = {}
		c.update(csrf(request))
		return render(request, 'register.html')
	else:
		messages.add_message(request, messages.WARNING, 'Accès interdit.')
		return HttpResponseRedirect('/home')


@login_required
def doRegister(request):
	if hasGroup(request.user, 'secretaire'):
		username=request.POST.get('username')
		if User.objects.filter(username=username).exists():
			messages.add_message(request, messages.ERROR, 'Identifiant existe déja!.')
			return HttpResponseRedirect('/profile/register')
		password = request.POST.get('password1')
		cpassword = request.POST.get('password2')
		if not password == cpassword:
			messages.add_message(request, messages.ERROR, 'Mots de passe incompatibles! .')
			return HttpResponseRedirect('/profile/register')
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		contact_no = request.POST.get('contact_no')
		if not contact_no.isdigit():
			messages.add_message(request, messages.ERROR, 'Contacte incorrecte! .')
			return HttpResponseRedirect('/profile/register')
		address = request.POST.get('address')
		dob = request.POST.get('dob')
		blood_group = request.POST.get('blood_group')
		CIN = request.POST.get('CIN')
		profession = request.POST.get('profession')
		sex = request.POST.get('sex')
		email = request.POST.get('email')
		patient = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
		patient.patient = Patient(contact_no=int(contact_no), address=address, dob=dob, blood_group=blood_group, CIN=CIN, sex=sex, profession=profession)
		patient.patient.save()
		patient.save()

		group = Group.objects.get(name='patient')
		group.user_set.add(patient)
		group.save()

		messages.add_message(request, messages.WARNING, 'Patient ajouté avec succès '+username)
		return HttpResponseRedirect('/case/generate')
	else:
		messages.add_message(request, messages.WARNING, 'Accès interdit.')
		return HttpResponseRedirect('/profile/register/')