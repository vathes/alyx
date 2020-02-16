# Generated by Django 2.2.6 on 2020-02-16 10:11

import django.contrib.postgres.fields.jsonb
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('actions', '0009_ephyssession'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProbeInsertion',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, help_text='Long name', max_length=255)),
                ('json', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Structured data, formatted in a user-defined way', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProbeModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, help_text='Long name', max_length=255)),
                ('json', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Structured data, formatted in a user-defined way', null=True)),
                ('probe_manufacturer', models.CharField(max_length=255)),
                ('probe_model', models.CharField(help_text="manufacturer's part number e.g. A4x8-5mm-100-20", max_length=255, unique=True)),
                ('description', models.CharField(blank=True, help_text="optional informal description e.g. 'Michigan 4x4 tetrode'; 'Neuropixels phase 2 option 1'", max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TrajectoryEstimate',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('x', models.FloatField(help_text='brain surface medio-lateral coordinate (um) ofthe insertion, right +, relative to Bregma', null=True, verbose_name='x-ml (um)')),
                ('y', models.FloatField(help_text='brain surface antero-posterior coordinate (um) of the insertion, front +, relative to Bregma', null=True, verbose_name='y-ap (um)')),
                ('z', models.FloatField(help_text='brain surface dorso-ventral coordinate (um) of the insertion, up +, relative to Bregma', null=True, verbose_name='z-dv (um)')),
                ('depth', models.FloatField(help_text='probe insertion depth (um)', null=True)),
                ('theta', models.FloatField(help_text='Polar angle ie. from vertical, (degrees) [0-180]', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(180)])),
                ('phi', models.FloatField(help_text='Azimuth from right (degrees), anti-clockwise, [0-360]', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(360)])),
                ('roll', models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(360)])),
                ('provenance', models.IntegerField(choices=[(70, 'Ephys aligned histology track'), (50, 'Histology track'), (30, 'Micro-manipulator'), (10, 'Planned')], default=10)),
                ('probe_insertion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trajectory_estimate', to='experiments.ProbeInsertion')),
            ],
        ),
        migrations.AddField(
            model_name='probeinsertion',
            name='model',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='experiments.ProbeModel'),
        ),
        migrations.AddField(
            model_name='probeinsertion',
            name='session',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='actions.EphysSession'),
        ),
        migrations.AddConstraint(
            model_name='trajectoryestimate',
            constraint=models.UniqueConstraint(fields=('provenance', 'probe_insertion'), name='unique_trajectory_per_provenance'),
        ),
        migrations.AddConstraint(
            model_name='probeinsertion',
            constraint=models.UniqueConstraint(fields=('name', 'session'), name='unique_probe_insertion_name_per_session'),
        ),
    ]
