import datetime
appointments = [
    {
        'id': 'appointment1',
        'startTime' : datetime.datetime(2021, 7, 17, 12, 15),
        'patient' : 'patient1',
        'appointment_type' : 'appointment_type1'
    },
    {
        'id': 'appointment2',
        'startTime' : datetime.datetime(2021, 7, 18, 12, 15),
        'patient' : 'patient2',
        'appointment_type' : 'appointment_type2',
        'pre_appointment_responses': [
            {
                'question': 'What is the issue?',
                'response': 'Nothing, just a little fat',
            },
            {
                'question': 'When did you start noticing the symptoms?',
                'response': 'My whole life',
            }
        ]
    },
    {
        'id': 'appointment3',
        'startTime' : datetime.datetime(2021, 7, 19, 12, 30),
        'patient' : 'patient3',
        'appointment_type' : 'appointment_type3',
        'pre_appointment_responses': [
            {
                'question': 'Have you gotten a flu shot before, and if so when was your last flu shot?',
                'response': 'No',
            }
        ]
    },
    {
        'id': 'appointment4',
        'startTime' : datetime.datetime(2021, 7, 19, 16, 15),
        'patient' : 'patient4',
        'appointment_type' : 'appointment_type4'
    },
    {
        'id': 'appointment5',
        'startTime' : datetime.datetime(2021, 7, 22, 13, 20),
        'patient' : 'patient4',
        'appointment_type' : 'appointment_type5',
        'pre_appointment_responses' : [
            {
                'question': 'What is the issue?',
                'response': 'My whole life'
            },
            {
                'question': 'When did you start noticing the symptoms?',
                'response': 'Been noticing them'
            }
        ]
    },
]
