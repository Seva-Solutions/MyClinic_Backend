# Generated by Django 3.0.6 on 2021-07-19 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0004_auto_20210718_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preappointmentquestion',
            name='question',
            field=models.CharField(default='', max_length=255),
        ),
    ]
