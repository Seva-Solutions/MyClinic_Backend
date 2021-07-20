from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from Atreya.patients.models import Patient 
from Atreya.patients.serializers import PatientSerializer
from rest_framework.authtoken.models import Token
from .data.patients import patients

class Command(BaseCommand):
    help = 'create/delete sample data'
    def add_arguments(self, parser):
        parser.add_argument('command', type=str, help='create/delete sample data')

    def handle(self, *args, **options):
        if options['command']== 'create':
            try:
                for patient in patients:
                    serializer = PatientSerializer(None, data=patient)
                    if serializer.is_valid():
                        patient = serializer.save()
                    else:
                        print(serializer.errors)
                        raise CommandError('failure in creating sample data')

            except Exception as e:
                print(e)
                raise CommandError('failure in creating sample data')
            self.stdout.write(self.style.SUCCESS('Successfully created data'))
        elif options["command"] ==  "delete":
            
            try:
                Patient.objects.all().delete()

            except Exception as e:
                print(e)
                raise CommandError('failure in deleting sample data')

            self.stdout.write(self.style.SUCCESS('Successfully deleted data'))
        else:
            raise CommandError("not a valid command")  
        