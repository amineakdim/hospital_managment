from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from .views import *

urlpatterns = [

    path('', profileUser),
    path('registerUser/', registerUser),
    path('doRegisterUser/', doRegisterUser),
   



    path('profileSec/', profileSec),
    path('registerSec/', registerSec),
    path('doRegisterSec/', doRegisterSec),
   
]