from django.test import TestCase
import requests
import logging
from .models import *
from .serializers import *
import json
import datetime

class patients_tests(TestCase):
    def save_patient(self, patient):
        serializer = PatientSerializer(None, data=patient)
        if serializer.is_valid():
            patient = serializer.save()
            print('\n patient saved \n')
        else:
            print(serializer.errors)
            raise Exception('failure in creating sample data')

    def test_patient(self):
        patient = {
            'id': 'patient1',
            'firstName' : 'Sailesh',
            'middleName' : '',
            'lastName' : 'Sharma',
            'dob': datetime.date(1998,3,4),
            'address' : '4732 Some other lane',
            'gender' : 'M',
            'email' : 'sailesh@sharma.com',
            'insuranceNumber' : '12312312',
            'verified' : True,
            'insuranceVerified' : True,
            'phoneNumber': '4164523905',
            'image' : '',
        }
        self.save_patient(patient)

        response = self.client.get('http://localhost:8000/patients/patient1')
        print(response.content)
        self.assertEqual(response.status_code, 200)