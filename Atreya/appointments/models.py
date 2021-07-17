from django.db import models

from Atreya.doctors.models import Doctor
from Atreya.clinics.models import Clinic
from Atreya.patients.models import Patient

# Create your models here.
class Appointment(models.Model):
    id = models.CharField(max_length=50,primary_key=True,default='')
    startTime = models.DateField()
    endTime = models.DateField()
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE,default=None)
    clinic_id = models.ForeignKey(Clinic, on_delete=models.CASCADE,default=None)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE,default=None)
    appointment_type = models.CharField(max_length=100)


    class Types(models.TextChoices):
        full_checkup = "full checkup"
        vitals_checkup = "vitals checkup"
        vaccination = "vaccination"
        prescription_refill = "prescription refill"
        general_consultation = "general consultation"
        other = "other"
    class Meta:
        ordering = ['id']
