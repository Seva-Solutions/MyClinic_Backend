# Generated by Django 3.0.6 on 2021-07-18 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0003_auto_20210718_2323'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PreAppointmentResponses',
            new_name='PreAppointmentResponse',
        ),
    ]