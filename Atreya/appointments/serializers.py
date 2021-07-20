from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class AppointmentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentType
        fields = '__all__'

class PreAppointmentQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreAppointmentQuestion
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

class PreAppointmentResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreAppointmentResponse
        fields = '__all__'