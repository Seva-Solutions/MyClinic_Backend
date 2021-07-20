from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from Atreya.appointments.models import * 
from Atreya.appointments.serializers import *
from rest_framework.authtoken.models import Token
from .data.appointment_types import appointment_types
from .data.appointments import appointments
from .data.pre_appointment_questions import pre_appointment_questions
from .data.pre_appointment_responses import pre_appointment_responses

class Command(BaseCommand):
    help = 'create/delete sample data'
    def add_arguments(self, parser):
        parser.add_argument('command', type=str, help='create/delete sample data')

    def handle(self, *args, **options):
        if options['command']== 'create':
            try:
                for appointment_type in appointment_types:
                    serializer = AppointmentTypeSerializer(None, data=appointment_type)
                    if serializer.is_valid():
                        appointment_type = serializer.save()
                    else:
                        print(serializer.errors)
                        raise CommandError('failure in creating sample data')

                for pre_appointment_question in pre_appointment_questions:
                    serializer = PreAppointmentQuestionSerializer(None, data=pre_appointment_question)
                    if serializer.is_valid():
                        pre_appointment_question = serializer.save()
                    else:
                        print(serializer.errors)
                        raise CommandError('failure in creating sample data')

                for appointment in appointments:
                    serializer = AppointmentSerializer(None, data=appointment)
                    if serializer.is_valid():
                        appointment = serializer.save()
                    else:
                        print(serializer.errors)
                        raise CommandError('failure in creating sample data')

                
                for pre_appointment_response in pre_appointment_responses:
                    serializer = PreAppointmentResponseSerializer(None, data=pre_appointment_response)
                    if serializer.is_valid():
                        pre_appointment_response = serializer.save()
                    else:
                        print(serializer.errors)
                        raise CommandError('failure in creating sample data')

            except Exception as e:
                print(e)
                raise CommandError('failure in creating sample data')
            self.stdout.write(self.style.SUCCESS('Successfully created data'))
        elif options["command"] ==  "delete":
            try:
                PreAppointmentResponse.objects.all().delete()
                Appointment.objects.all().delete()
                PreAppointmentQuestion.objects.all().delete()
                AppointmentType.objects.all().delete()

            except Exception as e:
                print(e)
                raise CommandError('failure in deleting sample data')

            self.stdout.write(self.style.SUCCESS('Successfully deleted data'))
        else:
            raise CommandError("not a valid command")  
        