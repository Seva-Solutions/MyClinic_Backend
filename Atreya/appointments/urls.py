from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('appointments/<str:appointment_id>',views.appointments),
    path('appointments/',views.appointments),
]

urlpatterns = format_suffix_patterns(urlpatterns)