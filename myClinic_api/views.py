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
