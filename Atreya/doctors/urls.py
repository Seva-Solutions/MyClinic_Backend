from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('doctors/total_doctors', views.total_doctors, name='total-doctors'),
    path('doctors/<int:doctor_id>',views.doctors),  
]

urlpatterns = format_suffix_patterns(urlpatterns)