# Generated by Django 3.0.6 on 2021-07-18 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0002_auto_20210718_0200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='image',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='patient',
            name='middleName',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
    ]