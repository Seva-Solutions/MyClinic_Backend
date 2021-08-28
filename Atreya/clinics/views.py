from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate, login, update_session_auth_hash
from rest_framework.authtoken.models import Token
from django.http import HttpResponse, JsonResponse
from django.http.request import HttpRequest
from .serializers import *
from .models import *
from django.contrib.auth.models import User

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
@api_view(['GET'])
@permission_classes((AllowAny,))
@csrf_exempt
def clinics(request, clinic_id=''):
    if request.method == "GET":
        clinic_view = None
        try:
            clinic_view = Clinic.objects.get(id=clinic_id)
        except Clinic.DoesNotExist:
            return Response(f'Clinic does not exist', status=404)
        serializer = ClinicSerializer(clinic_view)
        return Response(serializer.data)
    # Both of these endpoints will not be used in first iteration
    elif request.method == 'POST':
        add_clinic = None
        serializer = ClinicSerializer(add_clinic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Clinic Sucessfully Added", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        clinic_id = clinic_id if clinic_id else request.GET.get('clinic', request.data['id'])
        try:
            clinic = Clinic.objects.get(id=clinic_id)
        except Clinic.DoesNotExist:
            return Response(f'Clinic does not exist', status=404)
        serializer = ClinicSerializer(clinic, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Clinic Sucessfully Updated", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST',])
@permission_classes((AllowAny,))
@csrf_exempt
def login_view(request):
    username = request.data['id']
    password = request.data['password']
    user = authenticate(request, username=username,password=password)
    if user is not None:
        #login(request,user)
        token, created = Token.objects.get_or_create(user=user)
        response = {
            'token': token.key
        }
        return Response(response)

    else:
        return HttpResponse('Invalid login', status=405)