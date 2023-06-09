# Generated by Django 4.1.7 on 2023-03-27 03:22

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shapedata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DRAINAGE_L',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Id', models.IntegerField()),
                ('RD_NAME', models.CharField(max_length='150')),
                ('CONSTRN_MA', models.CharField(max_length='150')),
                ('CATEGORY', models.CharField(max_length='50')),
                ('PHOTO', models.CharField(max_length='150')),
                ('geom', django.contrib.gis.db.models.fields.LineStringField(srid=4326)),
            ],
            options={
                'db_table': 'drainage_l',
            },
        ),
        migrations.DeleteModel(
            name='Road',
        ),
    ]
