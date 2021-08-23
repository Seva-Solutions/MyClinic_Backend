from django.test import TestCase
import requests
import logging
from .models import *
import json
import datetime
from django.core.management import call_command

class appointments_tests(TestCase):
    def __init__(self, *args):
        super().__init__(*args)

    def setUp(self) -> None:
        call_command('patients', 'create')
        call_command('doctors', 'create')
        call_command('clinics', 'create')
        call_command('appointments', 'create')
        return super().setUp()

    def test_appointments_by_clinic_id(self):
        response = self.client.get('http://localhost:8000/appointments/?clinic=clinic1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 4)

    def test_appointments_by_doctor_id(self):
        response = self.client.get('http://localhost:8000/appointments/?doctor=doctor1')
        expected_response = [
            {"id": 1, "startTime":"2021-07-17T12:15:00Z","patient":"patient1","appointment_type":"appointment_type1","endTime":"2021-07-17T12:45:00Z"},
            {"id": 2, "startTime":"2021-07-18T12:15:00Z","patient":"patient2","appointment_type":"appointment_type2","endTime":"2021-07-18T13:00:00Z"},
            {"id": 3, "startTime":"2021-07-19T12:30:00Z","patient":"patient3","appointment_type":"appointment_type3","endTime":"2021-07-19T12:45:00Z"}
        ]
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.json()[0], expected_response[0])
        self.assertDictEqual(response.json()[1], expected_response[1])
        self.assertDictEqual(response.json()[2], expected_response[2])

    def test_appointments_by_date_range(self):
        start = '2021-07-17T12%3A15%3A00Z'
        end = '2021-07-19T12%3A29%3A00Z'
        doctor = 'doctor1'
        response = self.client.get(f'http://localhost:8000/appointments/?start={start}&end={end}&doctor={doctor}')
        expected_response = [
            {"id": 1, "startTime":"2021-07-17T12:15:00Z","patient":"patient1","appointment_type":"appointment_type1","endTime":"2021-07-17T12:45:00Z"},
            {"id": 2, "startTime":"2021-07-18T12:15:00Z","patient":"patient2","appointment_type":"appointment_type2","endTime":"2021-07-18T13:00:00Z"}
        ]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertDictEqual(response.json()[0], expected_response[0])
        self.assertDictEqual(response.json()[1], expected_response[1])

    def test_appointments_add_appointment(self):
        appointment = {
            'startTime' : datetime.datetime(2021, 7, 19, 16, 15),
            'patient' : 'patient4',
            'appointment_type' : 'appointment_type4'
        }

        response = self.client.post('http://localhost:8000/appointments/', data=appointment, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        id = response.json()['id']

        response = self.client.get(f'http://localhost:8000/appointments/{id}')
        expected_response = {"id": id,
                            "startTime":"2021-07-19T16:15:00Z",
                            "patient":"patient4",
                            "appointment_type":"appointment_type4",
                            "endTime":"2021-07-19T16:45:00Z"}
        self.assertDictEqual(response.json()[0], expected_response)

    def test_appointments_edit_appointment(self):
        appointment = {
            'startTime' : datetime.datetime(2021, 7, 19, 16, 15),
            'patient' : 'patient4',
            'appointment_type' : 'appointment_type4'
        }

        response = self.client.post('http://localhost:8000/appointments/', data=appointment, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        id = response.json()['id']

        response = self.client.get(f'http://localhost:8000/appointments/{id}')
        expected_response = {"id": id,
                            "startTime":"2021-07-19T16:15:00Z",
                            "patient":"patient4",
                            "appointment_type":"appointment_type4",
                            "endTime":"2021-07-19T16:45:00Z"}
        self.assertDictEqual(response.json()[0], expected_response)

        appointment = {
            "id": id,
            'startTime' : datetime.datetime(2021, 7, 19, 17, 15),
            'patient' : 'patient4',
            'appointment_type' : 'appointment_type4'
        }

        response = self.client.patch('http://localhost:8000/appointments/', data=appointment, content_type='application/json')
        self.assertEqual(response.status_code, 201)

        response = self.client.get(f'http://localhost:8000/appointments/{id}')
        expected_response = {
                            "id": id,
                            "startTime":"2021-07-19T17:15:00Z",
                            "patient":"patient4",
                            "appointment_type":"appointment_type4",
                            "endTime":"2021-07-19T17:45:00Z"}
        self.assertDictEqual(response.json()[0], expected_response)

    def test_appointments_add_appointment_with_responses(self):
        appointment = {
            'startTime' : datetime.datetime(2021, 7, 19, 16, 15),
            'patient' : 'patient4',
            'appointment_type' : 'appointment_type4',
            'pre_appointment_responses': [
            {
                'question': 'pre_appointment_question3',
                'response': 'No',
            }
        ]
        }

        response = self.client.post('http://localhost:8000/appointments/', data=appointment, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        id = response.json()['id']

        response = self.client.get(f'http://localhost:8000/appointments/{id}')
        expected_response = {"id": id,
                            "startTime":"2021-07-19T16:15:00Z",
                            "patient":"patient4",
                            "appointment_type":"appointment_type4",
                            "endTime":"2021-07-19T16:45:00Z"}
        self.assertDictEqual(response.json()[0], expected_response)