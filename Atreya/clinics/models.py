from django.db import models

# Create your models here.
class Clinic(models.Model):
    id = models.CharField(max_length=50,primary_key=True,default='')
    name = models.CharField(max_length=100)
    days = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    clinic_license = models.CharField(max_length=30)
    isLicenseVerified = models.BooleanField(default=False)
    password = models.CharField(max_length=30)

    class Meta:
        ordering = ['id']