# Generated by Django 4.2.6 on 2023-10-19 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0005_rename_sensor_measurement_sensor_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='img',
            field=models.ImageField(blank=True, upload_to=None),
        ),
    ]
