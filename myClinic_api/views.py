from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import *
from .models import *

# Create your views here.
@api_view(['GET',])
def total_numberofpatients(request):

    patient_view = None
    try:
        patient_view = Patient.objects.all().count()
    except Patient.DoesNotExist:
        return Response(f'Patients do not exist', status=404)

    if request.method == "GET":
        patient_view = Patient.objects.all().count()

    return Response(patient_view, status=status.HTTP_200_OK)

@api_view(['GET',])
def total_numberofclinics(request):

    clinic_view = None
    try:
        clinic_view = Clinic.objects.all().count()
    except Patient.DoesNotExist:
        return Response(f'Clinics do not exist', status=404)

    if request.method == "GET":
        clinic_view = Clinic.objects.all().count()

    return Response(clinic_view, status=status.HTTP_200_OK)

@api_view(['GET',])
def total_numberofdoctors(request):

    doctor_view = None
    try:
        doctor_view = Doctor.objects.all().count()
    except Patient.DoesNotExist:
        return Response(f'Doctors do not exist', status=404)

    if request.method == "GET":
        doctor_view = Doctor.objects.all().count()

    return Response(doctor_view, status=status.HTTP_200_OK)