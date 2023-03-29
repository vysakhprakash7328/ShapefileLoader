# Generated by Django 4.1.7 on 2023-03-28 04:26

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shapedata', '0067_final_road_chirakkal'),
    ]

    operations = [
        migrations.CreateModel(
            name='PANCHAYAT_BOUNDARY',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OBJECTID', models.IntegerField()),
                ('Id', models.IntegerField()),
                ('Shape_Leng', models.FloatField()),
                ('Shape_Area', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
            ],
            options={
                'db_table': 'panchayat_boundary',
            },
        ),
    ]
