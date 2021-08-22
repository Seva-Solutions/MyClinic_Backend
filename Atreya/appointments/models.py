from django.db import models

from Atreya.doctors.models import Doctor
from Atreya.clinics.models import Clinic
from Atreya.patients.models import Patient

class AppointmentType(models.Model):
    id = models.CharField(max_length=50,primary_key=True,default='')
    title = models.CharField(max_length=50,default='')
    length = models.IntegerField() #Length in minutes
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,default=None)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE,default=None)
    
    class Meta:
        ordering = ['id']

    def __str__(self):
           return self.title

class PreAppointmentQuestion(models.Model):
    id = models.CharField(max_length=50,primary_key=True,default='')
    question = models.CharField(max_length=255,default='')
    appointment_type = models.ForeignKey(AppointmentType, on_delete=models.CASCADE,default=None)
    
    class Meta:
        ordering = ['id']

    def __str__(self):
           return self.question
    
class Appointment(models.Model): 
    # id = models.CharField(max_length=50,primary_key=True,default='')
    startTime = models.DateTimeField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,default=None)
    appointment_type = models.ForeignKey(AppointmentType, on_delete=models.CASCADE,default=None)

    class Meta:
        ordering = ['id']

    def __str__(self):
           return self.appointment_type.title + ': ' + self.patient.firstName + ' ' + self.patient.lastName

class PreAppointmentResponse(models.Model):
    # id = models.CharField(max_length=50,primary_key=True,default='')
    question = models.ForeignKey(PreAppointmentQuestion, on_delete=models.CASCADE,default=None)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE,default=None)
    response = models.TextField(blank=True, null=True, default='')
    
    class Meta:
        ordering = ['id']

    def __str__(self):
           return self.response