from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from patients.models import Patients 
from rest_framework.authtoken.models import Token


class Command(BaseCommand):
    help = 'create/delete sample data'
    def add_arguments(self, parser):
        parser.add_argument('command', type=str, help='create/delete sample data')

    def handle(self, *args, **options):
        if options['command']== 'create':
            try:
                superuser = User.objects.create_superuser(
                username="admin",
                email="",
                password="Krishna123")
                superuser.save()

                for i, username in enumerate(contractorusernames):
                    contractor=Contractor.objects.create(id=username+contractorpasswords[i],firstName=username, lastName=contractorpasswords[i], 
                                                    workerNumber= "9051234567",
                                                    insuranceNumber="9059876543",
                                                    profileImageObjectStoreRef= "sample/"+contractorimages[i],
                                                    serviceList=contractorservicelist[i],
                                                    contractorLongitude=contractorlong[i],
                                                    contractorLatitude= contractorlat[i],
                                                    contractorAddress="1 Main Street",
                                                    contractorDevices="152.119.245.148,156.203.215.46,171.11.193.95",
                                                    mediaListObjectStoreRef="images/test1,images/test2")
                    user = User.objects.create_user(username=username, password=contractorpasswords[i])
                    contractor.save()
                    user.save()
                    userext = Profile.objects.get(user=user)
                    serializer = ProfileSerializer(userext, data={"contractor":contractor.pk}, partial=True)
                    if serializer.is_valid():
                        serializer.save() 
                for i, username in enumerate(clientusernames):
                    user = User.objects.create_user(username=username, password=clientpasswords[i])
                    client=Client.objects.create(id=username+clientpasswords[i],firstName=username, lastName=clientpasswords[i], clientDevices="152.119.245.148,156.203.215.46,171.11.193.95", profileImageObjectStoreRef ="sample/"+clientimages[i], email="test@gmail.com")
                    user.save()
                    client.save()
                    userext = Profile.objects.get(user=user)
                    serializer = ProfileSerializer(userext, data={"client":client.pk}, partial=True)
                    if serializer.is_valid():
                        serializer.save()

            except:
                raise CommandError('failure in creating sample data')
            self.stdout.write(self.style.SUCCESS('Successfully created data'))
        elif options["command"] ==  "delete":
            
            try:
                User.objects.all().delete()
                Client.objects.all().delete()
                Contractor.objects.all().delete()
                Message.objects.all().delete()

            except:
                raise CommandError('failure in deleting sample data')

            self.stdout.write(self.style.SUCCESS('Successfully deleted data'))
        else:
            raise CommandError("not a valid command")  
        