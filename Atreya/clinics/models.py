from django.db import models
from Atreya.doctors.models import Doctor

# Create your models here.
class Clinic(models.Model):
    id = models.CharField(max_length=50,primary_key=True,default='')
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, default=None, blank=True)
    email = models.CharField(max_length=100, default=None, blank=True)
    license = models.CharField(max_length=30)
    isLicenseVerified = models.BooleanField(default=False)
    password = models.CharField(max_length=30)
    doctors = models.ManyToManyField(Doctor, default=None, blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
           return self.name