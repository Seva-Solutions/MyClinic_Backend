from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

