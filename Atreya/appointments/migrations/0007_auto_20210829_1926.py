# Generated by Django 3.0.6 on 2021-08-29 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0006_auto_20210822_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preappointmentquestion',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
