from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = '__all__'
