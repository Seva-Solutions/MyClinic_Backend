# Generated by Django 3.0.6 on 2021-07-24 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0003_auto_20210717_2324'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorType',
            fields=[
                ('id', models.CharField(default='', max_length=50, primary_key=True, serialize=False)),
                ('type', models.CharField(default='', max_length=75)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
