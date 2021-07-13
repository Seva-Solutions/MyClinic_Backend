from django.urls import include, path
from rest_framework import routers
from . import views

from myClinic_api.views import (
     total_numberofpatients,
     total_numberofclinics,
     total_numberofdoctors
)
   
app_name = 'myClinic_api'

urlpatterns = [

    #endpoints to get total number of items
    path('get_totalpatients/', total_numberofpatients),
    path('get_totalclinics/', total_numberofclinics),
    path('get_totaldoctors/', total_numberofdoctors),
]