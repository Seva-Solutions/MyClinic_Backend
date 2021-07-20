# Generated by Django 3.0.6 on 2021-07-18 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0003_auto_20210717_2324'),
        ('clinics', '0004_clinic_doctors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinic',
            name='doctors',
            field=models.ManyToManyField(blank=True, default=None, to='doctors.Doctor'),
        ),
    ]
