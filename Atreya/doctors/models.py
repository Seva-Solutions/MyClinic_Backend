from django.db import models

# Create your models here.


class Doctor(models.Model):
    id = models.CharField(max_length=50,primary_key=True,default='')
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    doctor_license = models.CharField(max_length=30)
    isLicenseVerified = models.BooleanField(default=False)
    specialty = models.CharField(max_length=50)
    gender = models.CharField(max_length=6)

    class Meta:
        ordering = ['id']
