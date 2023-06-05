from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, Group
from .models import *

from datetime import datetime
from home.context_processors import hasGroup
from case.models import case
from django.contrib import messages
# Create your views here.

#CREATE
@login_required
def generate(request, case_id):
    if hasGroup(request.user, 'secretaire'):
        c = {}
        c.update(csrf(request))
        c['case'] = case.objects.get(id=int(case_id))
        c['actes'] = actes.objects.all()
        return render(request, 'facture/generate.html', c)
    messages.add_message(request, messages.WARNING, 'Accès refusé.')
    return HttpResponseRedirect('home/')

@login_required
def doGenerate(request):
    if hasGroup(request.user, 'secretaire'):
        c = case.objects.get(id=request.POST.get('case', ''))
        acte = actes.objects.get(id=request.POST.get('acte', ''))
        quantite = int(request.POST.get('quantite', ''))
        facture_date = datetime.now()
        facture_details = request.POST.get('description', '')
        ammount = acte.sell_price* quantite
        b = facture(case=c, acte=acte, quantite=quantite, facture_date=facture_date, facture_details=facture_details, ammount=ammount)
        b.save()
        messages.add_message(request, messages.INFO, 'Consultation ajoutée avec succès.')
        return HttpResponseRedirect('/case/')
    messages.add_message(request, messages.WARNING, 'Accès refusé.')
    return HttpResponseRedirect('/home/')

#RETRIEVE
@login_required
def view(request):
    c = {}
    c.update(csrf(request))
    if hasGroup(request.user, 'patient'):
        c['factures'] = []
        c['isPatient'] = True
        for cases in case.objects.filter(patient=request.user):
            c['factures'].extend(list(facture.objects.filter(case=cases)))
    elif hasGroup(request.user, 'secretaire'):
        id = request.POST.get('patient', '')
        if id == '':
            c['selectPatient'] = True
            c['patients'] = User.objects.filter(groups__name='patient')
            return render(request, 'facture/view_facture.html', c)
        else:
            c['factures'] = []
            for cases in case.objects.filter(patient=User(id=id)):
                c['factures'].extend(list(facture.objects.filter(case=cases)))
    else:
        messages.add_message(request, messages.WARNING, 'Accès refusé.')
        return HttpResponseRedirect('/home')

    factures = c['factures']
    c['paidfactures'] = []
    c['pendingfactures'] = []
    for b in factures:
        if b.is_paid:
            c['paidfactures'].append(b)
        else:
            c['pendingfactures'].append(b)
    return render(request, 'facture/view_facture.html', c)

@login_required
def viewMedicine(request):
    c = {}
    if hasGroup(request.user, 'patient'):
        c['factures'] = []
        c['isPatient'] = True
        for cases in case.objects.filter(patient=request.user):
            c['factures'].extend(list(facture.objects.filter(case=cases)))
        return render(request, 'facture/medicines.html', c)
    else:
        messages.add_message(request, messages.WARNING, 'Accès refusé.')
        return HttpResponseRedirect('/home')

#UPDATE
@login_required
def pay(request):
    user = request.user
    if hasGroup(user, 'secretaire'):
        ids = request.POST.getlist('ids','123')
        if type(ids)==type([]):
            for id in ids:
                b = facture.objects.get(id=int(id))
                b.is_paid = True
                b.save()
        else:
            b = facture.objects.get(id=int(ids))
            b.is_paid = True
            b.save()
        messages.add_message(request, messages.INFO, 'facture Payée avec succès.')
        return HttpResponseRedirect('/facture/')
    messages.add_message(request, messages.WARNING, 'Accès refusé.')
    return HttpResponseRedirect('/home')

#DELETE
@login_required
def delete(request, id):
    user = request.user
    if hasGroup(user, 'secretaire'):
        facture.objects.get(id=id).delete()
        messages.add_message(request, messages.INFO, 'Facture supprimée avec succès.')
        return HttpResponseRedirect('/facture/')
    messages.add_message(request, messages.WARNING, 'Accès refusé.')
    return HttpResponseRedirect('/home')
