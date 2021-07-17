# Generated by Django 3.0.6 on 2021-07-17 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.CharField(default='', max_length=50, primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
                ('doctor_license', models.CharField(max_length=30)),
                ('isLicenseVerified', models.BooleanField(default=False)),
                ('specialty', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=6)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]