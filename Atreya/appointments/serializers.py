# from typing_extensions import Required
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
import datetime


class AppointmentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentType
        fields = '__all__'
    
    def create(self, validated_data):
        # import pdb; pdb.set_trace()
        instance = AppointmentType.objects.create(**validated_data)
        return instance

class PreAppointmentQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreAppointmentQuestion
        fields = '__all__'

class PreAppointmentResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreAppointmentResponse
        fields = '__all__'
    
    def validate(self, data):
        return data

class AppointmentSerializer(serializers.ModelSerializer):
    pre_appointment_responses = PreAppointmentResponseSerializer(required=False, many=True)

    class Meta:
        model = Appointment
        fields = '__all__'
    
    def validate(self, data):
        return data

    def create(self, validated_data):
        responses = []
        if 'pre_appointment_responses' in validated_data:
            responses = validated_data.pop('pre_appointment_responses')
        instance = Appointment.objects.create(**validated_data)
        for response in responses:
            resp = PreAppointmentResponse(response=response['response'], question=response['question'], appointment=instance)
            try:
                resp.save()
            except Exception as e:
                print(e)
        return instance

    # def update(self, instance, validated_data):
    #     if 'languageList' in validated_data:
    #         instance.languageList.clear()
    #         languages = validated_data.pop('languageList')
    #         for new_language in languages:
    #             instance.languageList.add(new_language)
    #     return super().update(instance, validated_data)

    def to_representation(self, instance):
        endTime = instance.startTime + datetime.timedelta(minutes=instance.appointment_type.length)
        representation = super(AppointmentSerializer, self).to_representation(instance) 
        representation['endTime'] = endTime
        return representation
