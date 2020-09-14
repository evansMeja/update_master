from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('api-data/', getdata, name="getdata"),
    path('delete-data/<int:pk>', deletedata, name="deletedata"),
    path('api-update/<int:pk>', apiupdate, name="apiupdate"),
]

