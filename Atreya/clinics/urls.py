from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('clinics/total_clinics', views.total_clinics, name='total-clinics'),
    path('clinics/<int:clinic_id>',views.clinics),
    path('clinics/get_nearby_clinics/<id>', nearby_clinics),  
]

urlpatterns = format_suffix_patterns(urlpatterns)