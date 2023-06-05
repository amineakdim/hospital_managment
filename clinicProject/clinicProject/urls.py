"""clinicProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from login.views import login, logout
from profiles.views import *
from users.views import profileUser, registerUser, doRegisterUser
from case.views import *

urlpatterns = [
	path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('users/', include('users.urls')),
    path('profile/', include('profiles.urls')),
 	path('login/', login),
 	path('login/', include('login.urls')),
 	path('logout/', logout),
    path('appointments/', include('appointments.urls')),
    path('case/', include('case.urls')),
    path('facture/', include('facture.urls')),
   

   
]
