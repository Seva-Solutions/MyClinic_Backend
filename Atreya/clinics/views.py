from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import *
from .models import *

@api_view(['GET',])
def total_clinics(request):

    clinic_view = None
    try:
        clinic_view = Clinic.objects.all().count()
    except Patient.DoesNotExist:
        return Response(f'Clinics do not exist', status=404)

    if request.method == "GET":
        clinic_view = Clinic.objects.all().count()

    return Response(clinic_view, status=status.HTTP_200_OK)

# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes((AllowAny,))
@csrf_exempt
def clinics(request):

    if request.method == "GET":
        clinic_view = None
        try:
            clinic_view = Clinic.objects.get(id=id)
        except Clinic.DoesNotExist:
            return Response(f'Clinic does not exist', status=404)
        serializer = ClinicSerializer(clinic_view,many=True)
    elif request.method == 'POST':
        add_clinic = None
        serializer = ClinicSerializer(add_clinic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Clinic Sucessfully Added", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
