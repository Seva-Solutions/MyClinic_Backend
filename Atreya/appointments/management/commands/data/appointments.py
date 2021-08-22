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
                'question': 'pre_appointment_question1',
                'response': 'Nothing, just a little fat',
            },
            {
                'question': 'pre_appointment_question2',
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
                'question': 'pre_appointment_question3',
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
                'question': 'pre_appointment_question4',
                'response': 'My whole life'
            },
            {
                'question': 'pre_appointment_question5',
                'response': 'Been noticing them'
            }
        ]
    },
]