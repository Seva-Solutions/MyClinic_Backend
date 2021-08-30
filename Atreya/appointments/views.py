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


# Create your views here.
@api_view(['GET', 'POST', 'PATCH'])
def appointment_types(request, appointment_type_id=''):
    add_appointment_type = None
    appointment_type_id = request.GET.get('appointment_type', appointment_type_id)
    if request.method == 'POST':
        serializer = AppointmentTypeSerializer(add_appointment_type, data=request.data)
        if serializer.is_valid():
            appointment_type = serializer.save()
            response = {'id' : appointment_type.id}
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        appointment_type_id = appointment_type_id if appointment_type_id else request.data['id']
        try:
            add_appointment_type = AppointmentType.objects.get(id=appointment_type_id)
        except AppointmentType.DoesNotExist:
            return Response(f'Appointment Type does not exist', status=404)
        serializer = AppointmentTypeSerializer(add_appointment_type, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Appointment Type Sucessfully Updated", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "GET":
        appointment_type_data = None
        clinic_id = request.GET.get('clinic', '')
        doctor_id = request.GET.get('doctor', '')

        if not clinic_id and not appointment_type_id and not doctor_id:
            return Response(f'Appointment type id, clinic id or doctor id must be specified', status=404)
        elif (clinic_id or doctor_id) and appointment_type_id:
            return Response(f'Please specify either appointment type id or one of; clinic id, doctor id. Not both', status=404)
        appointment_type_data = AppointmentType.objects

        if clinic_id and doctor_id:
            appointment_type_data = appointment_type_data.filter(clinic__id=clinic_id, doctor__id=doctor_id)
        elif clinic_id:
            appointment_type_data = appointment_type_data.filter(clinic__id=clinic_id)
        elif doctor_id:
            appointment_type_data = appointment_type_data.filter(doctor__id=doctor_id)
        else:
            try:
                appointment_type_data = [ AppointmentType.objects.get(id=appointment_type_id) ]
            except Appointment.DoesNotExist:
                return Response(f'Appointment does not exist', status=404)
        serializer = AppointmentTypeSerializer(appointment_type_data,many=True)
        return Response(serializer.data)


# Create your views here.
@api_view(['GET', 'POST', 'PATCH'])
def pre_appointment_questions(request, pre_appointment_question_id=''):
    add_pre_appointment_question = None
    pre_appointment_question_id = request.GET.get('pre_appointment_question', pre_appointment_question_id)
    if request.method == 'POST':
        serializer = PreAppointmentQuestionSerializer(add_pre_appointment_question, data=request.data)
        if serializer.is_valid():
            pre_appointment_question = serializer.save()
            response = {'id' : pre_appointment_question.id}
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        pre_appointment_question_id = pre_appointment_question_id if pre_appointment_question_id else request.data['id']
        try:
            add_pre_appointment_question = PreAppointmentQuestion.objects.get(id=pre_appointment_question_id)
        except PreAppointmentQuestion.DoesNotExist:
            return Response(f'Appointment Type does not exist', status=404)
        serializer = PreAppointmentQuestionSerializer(add_pre_appointment_question, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Appointment Type Sucessfully Updated", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "GET":
        pre_appointment_question_data = None
        clinic_id = request.GET.get('clinic', '')
        doctor_id = request.GET.get('doctor', '')

        if not clinic_id and not pre_appointment_question_id and not doctor_id:
            return Response(f'Appointment type id, clinic id or doctor id must be specified', status=404)
        elif (clinic_id or doctor_id) and pre_appointment_question_id:
            return Response(f'Please specify either appointment type id or one of; clinic id, doctor id. Not both', status=404)
        pre_appointment_question_data = PreAppointmentQuestion.objects

        if clinic_id and doctor_id:
            pre_appointment_question_data = pre_appointment_question_data.filter(clinic__id=clinic_id, doctor__id=doctor_id)
        elif clinic_id:
            pre_appointment_question_data = pre_appointment_question_data.filter(clinic__id=clinic_id)
        elif doctor_id:
            pre_appointment_question_data = pre_appointment_question_data.filter(doctor__id=doctor_id)
        else:
            try:
                pre_appointment_question_data = [ PreAppointmentQuestion.objects.get(id=pre_appointment_question_id) ]
            except Appointment.DoesNotExist:
                return Response(f'Appointment does not exist', status=404)
        serializer = PreAppointmentQuestionSerializer(pre_appointment_question_data,many=True)
        return Response(serializer.data)
