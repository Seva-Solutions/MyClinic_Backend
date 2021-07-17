from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import *
from .models import *

# Create your views here.
@api_view(['POST',])
def appointments(request):
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
def get_appointment(request):
    if request.method == "GET":
        appointment_view = None
        try:
            appointment_view = Appointment.objects.get(id=id)
        except Appointment.DoesNotExist:
            return Response(f'Appointment does not exist', status=404)
        serializer = AppointmentSerializer(appointment_view,many=True)


