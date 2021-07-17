from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import *
from .models import *

# Create your views here.
@api_view(['GET',])
def total_patients(request):
    total_patients = None
    try:
        total_patients = Patient.objects.all().count()
    except Patient.DoesNotExist:
        return Response(f'Something went wrong', status=404)

    return Response(total_patients, status=status.HTTP_200_OK)


# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes((AllowAny,))
@csrf_exempt
def patients(request):
    if request.method == "GET":
        patient_view = None
        try:
            patient_view = Patient.objects.get(id=id)
        except Patient.DoesNotExist:
            return Response(f'Patient does not exist', status=404)
        serializer = PatientSerializer(patient_view,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        add_patient = None
        serializer = PatientSerializer(add_patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Patient Sucessfully Added", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


