# Generated by Django 4.1.7 on 2023-03-28 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shapedata', '0055_panchayat_boundary'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DRAINAGE_L',
        ),
        migrations.DeleteModel(
            name='PANCHAYAT_BOUNDARY',
        ),
        migrations.DeleteModel(
            name='Road',
        ),
    ]
