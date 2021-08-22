from django.db import models

# Create your models here.

class DoctorType(models.Model):
    id = models.CharField(max_length=50,primary_key=True,default='')
    type = models.CharField(max_length=75,default='')
    
    class Meta:
        ordering = ['id']

    def __str__(self):
           return self.type

class Doctor(models.Model):
    id = models.CharField(max_length=50,primary_key=True,default='')
    firstName = models.CharField(max_length=30)
    middleName = models.CharField(max_length=30, blank=True, default='')
    lastName = models.CharField(max_length=30)
    license = models.CharField(max_length=30)
    degree = models.CharField(max_length=30)
    types = models.ManyToManyField(DoctorType, default=None, blank=True)
    gender = models.CharField(max_length=6)

    class Meta:
        ordering = ['id']

    def __str__(self):
           return self.firstName + ' ' + self.lastName
