from django.contrib.auth.models import Group


def hasGroup(user, groupName):
    group = Group.objects.get(name=groupName)
    return True if group in user.groups.all() else False


def menu_processor(request):
    menu = {}
    user = request.user
    if hasGroup(user, 'doctor'):
        menu['Appointments'] = '/appointments'
        menu['Cases'] = '/case'
    elif hasGroup(user, 'patient'):
        menu['Reports'] = '/reports'
        menu['Appointments'] = '/appointments'
        menu['Medication'] = '/bill/medicines'
        menu['Bills'] = '/bill'
        menu['Cases'] = '/case'
    elif hasGroup(user, 'secretaire'):
        menu['New Patient'] = '/profile/register'
        menu['Manage Appointments'] = '/appointments'
        menu['New Appointment'] = '/appointments/book'
        menu['Bills'] = '/bill'
        menu['Cases'] = '/case'
        menu['Generate Case'] = '/case/generate'
    

    return {'menu': menu}