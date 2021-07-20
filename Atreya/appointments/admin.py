from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(AppointmentType)
admin.site.register(PreAppointmentQuestion)
admin.site.register(Appointment)
admin.site.register(PreAppointmentResponse) 