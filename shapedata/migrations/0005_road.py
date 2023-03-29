# Generated by Django 4.1.7 on 2023-03-27 03:27

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shapedata', '0004_drainage_l'),
    ]

    operations = [
        migrations.CreateModel(
            name='Road',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OBJECTID_1', models.IntegerField()),
                ('OBJECTID', models.IntegerField()),
                ('Rd_ID', models.CharField(max_length='15')),
                ('Code', models.CharField(max_length='10')),
                ('Sub_Class', models.CharField(max_length='30')),
                ('Length_Km', models.FloatField()),
                ('Ward_No', models.IntegerField()),
                ('Rd_Name', models.CharField(max_length='100')),
                ('Cons_Mat', models.CharField(max_length='30')),
                ('CW_Width', models.FloatField()),
                ('ROW_Width', models.FloatField()),
                ('Maintain', models.CharField(max_length='20')),
                ('FP', models.CharField(max_length='10')),
                ('FP_Width', models.FloatField()),
                ('FP_Cons_Ma', models.CharField(max_length='20')),
                ('FP_Place', models.CharField(max_length='10')),
                ('Start_Poin', models.CharField(max_length='150')),
                ('End_Point', models.CharField(max_length='150')),
                ('Photo', models.CharField(max_length='150')),
                ('Remarks', models.CharField(max_length='150')),
                ('Surveyor', models.CharField(max_length='50')),
                ('GlobalID', models.CharField(max_length='38')),
                ('CreationDa', models.DateField()),
                ('Creator', models.CharField(max_length='128')),
                ('EditDate', models.DateField()),
                ('Editor', models.CharField(max_length='128')),
                ('SHAPE_Leng', models.FloatField()),
                ('Remarks_1', models.CharField(max_length='50')),
                ('UNIQUE_ID', models.CharField(max_length='50')),
                ('RESHAPE', models.CharField(max_length='50')),
                ('Shape_Le_1', models.FloatField()),
                ('BUFF', models.CharField(max_length='50')),
                ('CHECK_V', models.CharField(max_length='50')),
                ('geom', django.contrib.gis.db.models.fields.LineStringField(srid=4326)),
            ],
            options={
                'db_table': 'road',
            },
        ),
    ]
