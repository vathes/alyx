# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-14 14:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0019_auto_20160112_1023'),
    ]

    operations = [
        migrations.CreateModel(
            name='Litter',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('father', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='litter_father', to='subjects.Litter')),
                ('mother', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='litter_mother', to='subjects.Litter')),
            ],
        ),
        migrations.AlterField(
            model_name='action',
            name='users',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='action',
            name='litter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='subjects.Litter'),
        ),
    ]