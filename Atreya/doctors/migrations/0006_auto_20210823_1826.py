# Generated by Django 3.0.6 on 2021-08-23 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0005_auto_20210724_0232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctortype',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
