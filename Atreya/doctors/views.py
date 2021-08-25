from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import *
from .models import *

@api_view(['GET',])
def total_doctors(request):
    doctor_view = None
    try:
        doctor_view = Doctor.objects.all().count()
    except Doctor.DoesNotExist:
        return Response(f'Doctors do not exist', status=404)

    if request.method == "GET":
        doctor_view = Doctor.objects.all().count()

    return Response(doctor_view, status=status.HTTP_200_OK)

# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes((AllowAny,))
@csrf_exempt
def doctors(request, doctor_id=''):
    if request.method == "GET":
        doctor_view = None
        try:
            doctor_view = Doctor.objects.get(id=doctor_id)
        except Doctor.DoesNotExist:
            return Response(f'Doctor does not exist', status=404)
        serializer = DoctorSerializer(doctor_view)
        return Response(serializer.data)
    elif request.method == 'POST':
        add_doctor = None
        serializer = DoctorSerializer(add_doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Doctor Sucessfully Added", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
