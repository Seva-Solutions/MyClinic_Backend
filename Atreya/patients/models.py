from django.db import models

# Create your models here.
class Patient(models.Model):
    id = models.CharField(max_length=50,primary_key=True,default='')
    firstName = models.CharField(max_length=30)
    middleName = models.CharField(max_length=30, blank=True, default='')
    lastName = models.CharField(max_length=30)
    dob = models.DateField()
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=6)
    email = models.EmailField(default=None)
    insuranceNumber = models.CharField(max_length=30)
    verified = models.BooleanField(default=False)
    insuranceVerified = models.BooleanField(default=False)
    phoneNumber = models.CharField(max_length=15, default='')
    image = models.CharField(max_length=100, default='', blank=True)
    class Meta:
        ordering = ['id']
