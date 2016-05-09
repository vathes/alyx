# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-09 15:32
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrainLocation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('stereotaxic_coordinates', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), size=3)),
                ('description', models.TextField()),
                ('allen_location_ontology', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CoordinateTransformation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('allen_location_ontology', models.CharField(max_length=1000)),
                ('origin', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), size=3)),
                ('transformation_matrix', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), size=3), size=3)),
            ],
        ),
    ]