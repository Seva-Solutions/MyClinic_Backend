from django.shortcuts import render
import json
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate, login, update_session_auth_hash
from rest_framework.authtoken.models import Token
from django.shortcuts import render
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.http.request import HttpRequest
from rest_framework import viewsets
from rest_framework.response import Response
from django.http.request import HttpRequest
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from .serializers import *
from .models import *
from django.http import HttpResponse

# Create your views here.

@api_view(['POST',])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def add_doctor(request):
    doctor_post = None
    if request.method != 'POST':
        return HttpResponse('Only the POST verb can be used on this endpoint.', status=405)
    elif request.method == 'POST':
        serializer = DoctorSerializer(add_doctor, data=request.data)
        if serealizer.is_valid():
            serializer.save()
            return Response("Doctor Successfully Added", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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


@api_view(['POST',])
def add_patient(request):
    add_patient = None
    if request.method != 'POST':
        return HttpResponse('Only the POST verb can be used on this endpoint.', status=405)
    elif request.method == 'POST':
        serializer = PatientSerializer(add_patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Patient Sucessfully Added", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST',])
def add_clinic(request):
    add_clinic = None
    if request.method != 'POST':
        return HttpResponse('Only the POST verb can be used on this endpoint.', status=405)
    elif request.method == 'POST':
        serializer = ClinicSerializer(add_clinic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Clinic Sucessfully Added", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST',])
def add_appointment(request):
    add_appointment = None
    if request.method != 'POST':
        return HttpResponse('Only the POST verb can be used on this endpoint.', status=405)
    elif request.method == 'POST':
        serializer = AppointmentSerializer(add_appointment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Appointment Sucessfully Added", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET',])
def clinic_view(request,id):

    clinic_view = None
    clinic_view= Clinic.objects.filter(id=id)

    if request.method == "GET":
        serializer = ClinicSerializer(clinic_view,many=True)
        return Response(serializer.data)

@api_view(['GET',])
@permission_classes((AllowAny,))
@csrf_exempt
def patient_view(request, id):
    patient_view = None
    try:
        patient_view = Patient.objects.get(id=id)
    except Patient.DoesNotExist:
        return Response(f'Patient does not exist', status=404)
    patient_view = Patient.objects.filter(id=id)
    if request.method == "GET":
        serializer = PatientSerializer(patient_view,many=True)
        return Response(serializer.data)

