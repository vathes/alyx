# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-29 10:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0003_auto_20170506_1823'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='otheraction',
            name='users',
        ),
        migrations.RemoveField(
            model_name='session',
            name='users',
        ),
        migrations.RemoveField(
            model_name='surgery',
            name='location',
        ),
        migrations.RemoveField(
            model_name='surgery',
            name='users',
        ),
        migrations.RemoveField(
            model_name='virusinjection',
            name='users',
        ),
        migrations.RemoveField(
            model_name='wateradministration',
            name='user',
        ),
        migrations.RemoveField(
            model_name='waterrestriction',
            name='users',
        ),
        migrations.RemoveField(
            model_name='weighing',
            name='user',
        ),
        migrations.AddField(
            model_name='otheraction',
            name='users',
            field=models.ManyToManyField(blank=True, help_text='The user(s) involved in this action', to='misc.OrderedUser'),
        ),
        migrations.AddField(
            model_name='session',
            name='users',
            field=models.ManyToManyField(blank=True, help_text='The user(s) involved in this action', to='misc.OrderedUser'),
        ),
        migrations.AddField(
            model_name='surgery',
            name='location',
            field=models.ForeignKey(blank=True, help_text='The physical location at which the surgery was performed', null=True, on_delete=django.db.models.deletion.CASCADE, to='equipment.LabLocation'),
        ),
        migrations.AddField(
            model_name='surgery',
            name='users',
            field=models.ManyToManyField(blank=True, help_text='The user(s) involved in this action', to='misc.OrderedUser'),
        ),
        migrations.AddField(
            model_name='virusinjection',
            name='users',
            field=models.ManyToManyField(blank=True, help_text='The user(s) involved in this action', to='misc.OrderedUser'),
        ),
        migrations.AddField(
            model_name='wateradministration',
            name='user',
            field=models.ForeignKey(blank=True, help_text='The user who administered water', null=True, on_delete=django.db.models.deletion.CASCADE, to='misc.OrderedUser'),
        ),
        migrations.AddField(
            model_name='waterrestriction',
            name='users',
            field=models.ManyToManyField(blank=True, help_text='The user(s) involved in this action', to='misc.OrderedUser'),
        ),
        migrations.AddField(
            model_name='weighing',
            name='user',
            field=models.ForeignKey(blank=True, help_text='The user who weighed the subject', null=True, on_delete=django.db.models.deletion.CASCADE, to='misc.OrderedUser'),
        ),

        migrations.DeleteModel(
            name='OrderedUser',
        ),

    ]
