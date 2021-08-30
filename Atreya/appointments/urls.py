from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('appointments/<str:appointment_id>',views.appointments),
    path('appointments/',views.appointments),
    path('appointments/types/',views.appointment_types),
    path('appointments/types/<str:appointment_type_id>',views.appointment_types),
    path('appointments/questions/',views.pre_appointment_questions),
    path('appointments/questions/<str:pre_appointment_question_id>',views.pre_appointment_questions),
    # path('appointments/types/<str:clinic_id>/<str:doctor_id>',views.appointment_types),
    # # path('appointments/types/<str:doctor_id>',views.appointment_types),
    # path('appointments/types/<str:doctor_id>/<str:clinic_id>',views.appointment_types), 
]

urlpatterns = format_suffix_patterns(urlpatterns)