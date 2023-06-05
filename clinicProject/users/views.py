from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,Group
from .models import Doctor, Secretaire
from django.template.context_processors import csrf
from home.context_processors import hasGroup
from django.contrib import messages


# Create your views here.
@login_required
def profileUser(request):
	c={}
	if request.user.is_superuser or hasGroup(request.user, 'doctor'):
		c['isPatient'] = True
	return render(request, 'profileUser.html')


@login_required
def profileSec(request):
	c={}
	if request.user.is_superuser or hasGroup(request.user, 'secretaire'):
		c['isPatient'] = True
	return render(request, 'profileSec.html')


@login_required
def registerUser(request):
	if request.user.is_superuser :
		c = {}
		c.update(csrf(request))
		return render(request, 'registerUser.html')
	else:
		messages.add_message(request, messages.WARNING, 'Access Denied.')
		return HttpResponseRedirect('/home')

@login_required
def registerSec(request):

	if request.user.is_superuser :
		c = {}
		c.update(csrf(request))
		return render(request, 'registerSec.html')
	else:
		messages.add_message(request, messages.WARNING, 'Access Denied.')
		return HttpResponseRedirect('/home')
    



@login_required
def doRegisterUser(request):
	if request.user.is_superuser :
		username = request.POST.get('username')
		if User.objects.filter(username=username).exists():
			messages.add_message(request, messages.ERROR, 'Username Already Exists.')
			return HttpResponseRedirect('/users/registerUser')
		password = request.POST.get('password1')
		cpassword = request.POST.get('password2')

		if not password == cpassword:
			messages.add_message(request, messages.ERROR, 'Passwords not matching.')
			return HttpResponseRedirect('/users/registerUser')
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		contact_no = request.POST.get('contact_no')
		if not contact_no.isdigit():
			messages.add_message(request, messages.ERROR, 'Wrong Contact no.')
			return HttpResponseRedirect('/users/registerUser')
		speciality = request.POST.get('speciality')
		sex = request.POST.get('sex')
		CIN = request.POST.get('CIN')
		email = request.POST.get('email')
		doctor = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
		doctor.doctor = Doctor(contact_no=int(contact_no), sex=sex, speciality=speciality, CIN=CIN)
		doctor.save()
		doctor.doctor.save()
    

		group = Group.objects.get(name='doctor')
		group.user_set.add(doctor)
		group.save()

		messages.add_message(request, messages.WARNING, 'Successfully Registered '+username)
		return HttpResponseRedirect('/home')
	else:
		messages.add_message(request, messages.WARNING, 'Access Denied.')
		return HttpResponseRedirect('/users/registerUser/')


@login_required
def doRegisterSec(request):
	if request.user.is_superuser :
		username = request.POST.get('username')
		if User.objects.filter(username=username).exists():
			messages.add_message(request, messages.ERROR, 'Username Already Exists.')
			return HttpResponseRedirect('/users/registerSec')
		password = request.POST.get('password1')
		cpassword = request.POST.get('password2')

		if not password == cpassword:
			messages.add_message(request, messages.ERROR, 'Passwords not matching.')
			return HttpResponseRedirect('/users/registerSec')
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		contact_no = request.POST.get('contact_no')
		if not contact_no.isdigit():
			messages.add_message(request, messages.ERROR, 'Wrong Contact no.')
			return HttpResponseRedirect('/users/registerSec')
		sex = request.POST.get('sex')
		CIN = request.POST.get('CIN')
		email = request.POST.get('email')
		secretaire = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
		secretaire.secretaire = Secretaire(contact_no=int(contact_no), sex=sex, CIN=CIN)
		secretaire.save()
		secretaire.secretaire.save()
    

		group = Group.objects.get(name='secretaire')
		group.user_set.add(secretaire)
		group.save()

		messages.add_message(request, messages.WARNING, 'Successfully Registered '+username)
		return HttpResponseRedirect('/home')
	else:
		messages.add_message(request, messages.WARNING, 'Access Denied.')
		return HttpResponseRedirect('/users/registerSec/')


