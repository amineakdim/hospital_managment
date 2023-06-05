from django.shortcuts import render,render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .context_processors import *
# Create your views here.
@login_required()
def home(request):
    messages.add_message(request, messages.INFO, 'Bienvenue.')
    return render(request, 'base.html')