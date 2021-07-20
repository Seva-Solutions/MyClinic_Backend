from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from Atreya.doctors.models import Doctor 
from Atreya.doctors.serializers import DoctorSerializer
from rest_framework.authtoken.models import Token
from .data.doctors import doctors

class Command(BaseCommand):
    help = 'create/delete sample data'
    def add_arguments(self, parser):
        parser.add_argument('command', type=str, help='create/delete sample data')

    def handle(self, *args, **options):
        if options['command']== 'create':
            try:
                for doctor in doctors:
                    serializer = DoctorSerializer(None, data=doctor)
                    if serializer.is_valid():
                        doctor = serializer.save()
                    else:
                        print(serializer.errors)
                        raise CommandError('failure in creating sample data')

            except Exception as e:
                print(e)
                raise CommandError('failure in creating sample data')
            self.stdout.write(self.style.SUCCESS('Successfully created data'))
        elif options["command"] ==  "delete":
            
            try:
                Doctor.objects.all().delete()

            except Exception as e:
                print(e)
                raise CommandError('failure in deleting sample data')

            self.stdout.write(self.style.SUCCESS('Successfully deleted data'))
        else:
            raise CommandError("not a valid command")  
        