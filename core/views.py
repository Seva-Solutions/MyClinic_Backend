from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .management.commands.data import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def patient_view(request):
    return JsonResponse(len(patients), safe=False)

@api_view(['GET'])
def doctor_view(request):
    return JsonResponse(len(doctors), safe=False)
    
@api_view(['GET'])
def clinic_view(request):
    return JsonResponse(len(clinics), safe=False)

def appointment_view(request):
    return JsonResponse({'appointments': appointments})




