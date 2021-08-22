from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('patients/total_patients', views.total_patients, name='total-patients'),
    path('patients/<str:patient_id>',views.patients),  
]

urlpatterns = format_suffix_patterns(urlpatterns)