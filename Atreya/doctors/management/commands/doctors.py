from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from Atreya.doctors.models import * 
from Atreya.doctors.serializers import *
from rest_framework.authtoken.models import Token
from .data.doctors import doctors
from .data.doctor_types import doctor_types

class Command(BaseCommand):
    help = 'create/delete sample data'
    def add_arguments(self, parser):
        parser.add_argument('command', type=str, help='create/delete sample data')

    def handle(self, *args, **options):
        if options['command']== 'create': 
            try:
                for doctor_type in doctor_types:
                    serializer = DoctorTypeSerializer(None, data=doctor_type)
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        print(serializer.errors)
                        raise CommandError('failure in creating sample data')

                for doctor in doctors:
                    serializer = DoctorSerializer(None, data=doctor)
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        print(serializer.errors)
                        raise CommandError('failure in creating sample data')

            except Exception as e:
                print(e)
                raise CommandError('failure in creating sample data')
            self.stdout.write(self.style.SUCCESS('Successfully created data'))
        elif options["command"] ==  "delete":
            
            try:
                DoctorType.objects.all().delete()
                Doctor.objects.all().delete()
            except Exception as e:
                print(e)
                raise CommandError('failure in deleting sample data')

            self.stdout.write(self.style.SUCCESS('Successfully deleted data'))
        else:
            raise CommandError("not a valid command")  
        