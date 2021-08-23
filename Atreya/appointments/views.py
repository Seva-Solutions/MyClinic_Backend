from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse, response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.utils.timezone import make_aware
from .serializers import *
from .models import *

# Create your views here.
@api_view(['GET', 'POST', 'PATCH'])
def appointments(request, appointment_id=''):
    add_appointment = None
    appointment_id = request.GET.get('appointment', appointment_id)
    if request.method == 'POST':
        serializer = AppointmentSerializer(add_appointment, data=request.data)
        if serializer.is_valid():
            appointment = serializer.save()
            response = {'id' : appointment.id}
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        appointment_id = request.GET.get('appointment', request.data['id'])
        try:
            add_appointment = Appointment.objects.get(id=appointment_id)
        except Appointment.DoesNotExist:
            return Response(f'Appointment does not exist', status=404)
        serializer = AppointmentSerializer(add_appointment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Appointment Sucessfully Updated", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "GET":
        appointment_data = None
        clinic_id = request.GET.get('clinic', '')
        doctor_id = request.GET.get('doctor', '')
        start = request.GET.get('start', '')
        end = request.GET.get('end', '')
        if not clinic_id and not appointment_id and not doctor_id:
            return Response(f'Appointment id, clinic id or doctor id must be specified', status=404)
        elif (clinic_id or doctor_id) and appointment_id:
            return Response(f'Please specify either appointment id or one of; clinic id, doctor id. Not both', status=404)
        elif appointment_id and (start or end):
            return Response(f'Date range cannot be used with appointment id.', status=404)

        start = make_aware(datetime.datetime.strptime(start, '%Y-%m-%dT%H:%M:%SZ')) if start else make_aware(datetime.datetime.now())-datetime.timedelta(weeks=520)
        end = make_aware(datetime.datetime.strptime(end, '%Y-%m-%dT%H:%M:%SZ')) if end else make_aware(datetime.datetime.now())+datetime.timedelta(weeks=520)
        appointment_data = Appointment.objects.filter(startTime__range=[start, end])

        if clinic_id and doctor_id:
            appointment_data = appointment_data.filter(appointment_type__clinic__id=clinic_id, appointment_type__doctor__id=doctor_id)
        elif clinic_id:
            appointment_data = appointment_data.filter(appointment_type__clinic__id=clinic_id)
        elif doctor_id:
            appointment_data = appointment_data.filter(appointment_type__doctor__id=doctor_id)
        else:
            try:
                appointment_data = [ Appointment.objects.get(id=appointment_id) ]
            except Appointment.DoesNotExist:
                return Response(f'Appointment does not exist', status=404)
        serializer = AppointmentSerializer(appointment_data,many=True)
        return Response(serializer.data)





