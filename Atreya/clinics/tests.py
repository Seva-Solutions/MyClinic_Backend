from django.test import TestCase
from django.core.management import call_command

# Create your tests here.
class doctors_tests(TestCase):
    def __init__(self, *args):
        super().__init__(*args)

    def setUp(self) -> None:
        call_command('patients', 'create')
        call_command('doctors', 'create')
        call_command('clinics', 'create')
        call_command('appointments', 'create')
        return super().setUp()

    def test_clinics_get_by_id(self):
        response = self.client.get('http://localhost:8000/clinics/clinic1')
        self.assertEqual(response.status_code, 200)
        expected_response = [
            {
                "id": "clinic1",
                "name": "General Family Health Clinic",
                "address":"4732 Some lane",
                "license":"23123some123license",
                "isLicenseVerified": False,
                "password":"Krishna123",
                "phone":'9053463459',
                "email": 'clinic1@atreya.ca',
                "doctors":["doctor1","doctor2"]
            }
        ]
        self.assertDictEqual(response.json(), expected_response[0])