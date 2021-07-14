from django.urls import include, path
from rest_framework import routers
from . import views

from myClinic_api.views import (
     total_numberofpatients,
     total_numberofclinics,
     total_numberofdoctors,
     add_patient,
     add_clinic
)
   
app_name = 'myClinic_api'

urlpatterns = [

    # Endpoints to get total number of items
    path('get_totalpatients/', total_numberofpatients),
    path('get_totalclinics/', total_numberofclinics),
    path('get_totaldoctors/', total_numberofdoctors),

    # Endpoint to add patients
    path('add_patient/add', add_patient),

      # Endpoint to add clinic
    path('add_clinic/add', add_clinic),
    
]   