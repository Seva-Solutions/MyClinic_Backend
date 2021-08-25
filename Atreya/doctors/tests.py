from django.test import TestCase
from django.core.management import call_command

class doctors_tests(TestCase):
    def __init__(self, *args):
        super().__init__(*args)

    def setUp(self) -> None:
        call_command('patients', 'create')
        call_command('doctors', 'create')
        call_command('clinics', 'create')
        call_command('appointments', 'create')
        return super().setUp()

    def test_doctors_get_by_id(self):
        response = self.client.get('http://localhost:8000/doctors/doctor1')
        self.assertEqual(response.status_code, 200)
        expected_response = [
            {
                'id': 'doctor1',
                'firstName' : 'Prawesh',
                'middleName' : '',
                'lastName' : 'Gaire',
                'license' : '23123123',
                'degree' : 'M.D.',
                'types' : ['Primary Care Physician (PCP)', 'OB-GYN (Obstetrician-Gynecologist)', 'Dermatologist'],
                'gender' : 'M',
            }
        ]
        self.assertDictEqual(response.json(), expected_response[0])