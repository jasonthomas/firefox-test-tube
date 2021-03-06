# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-15 23:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_observations', models.IntegerField()),
                ('population', models.CharField(max_length=255)),
                ('subgroup', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DataSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('slug', models.CharField(max_length=255, unique=True)),
                ('created_at', models.DateTimeField(null=True)),
                ('date', models.DateField()),
                ('display', models.BooleanField(default=False)),
                ('enabled', models.BooleanField(default=False)),
                ('import_start', models.DateTimeField(null=True)),
                ('import_stop', models.DateTimeField(null=True)),
            ],
            options={
                'get_latest_by': 'created_at',
            },
        ),
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, default='')),
                ('tooltip', models.CharField(blank=True, help_text='The tooltip displayed on hover. Available variables are: {x} - the x-axis label (if categorical) or value, {y} - the y-axis value which will be the summed proportions, and {p} - the individual proportion for the hovered data point.', max_length=255)),
                ('type', models.CharField(blank=True, default='', max_length=50)),
                ('units', models.CharField(blank=True, default='', max_length=50)),
                ('source_name', models.CharField(help_text="The metric's name in the source telemetry data.", max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bucket', models.CharField(max_length=255)),
                ('proportion', models.FloatField()),
                ('count', models.BigIntegerField(null=True)),
                ('rank', models.IntegerField(null=True)),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='_points', to='api.Collection')),
            ],
        ),
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('population', models.CharField(default='', max_length=255)),
                ('subgroup', models.CharField(default='', max_length=255)),
                ('key', models.CharField(max_length=100)),
                ('value', models.IntegerField()),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.DataSet')),
                ('metric', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Metric')),
            ],
        ),
        migrations.AddField(
            model_name='collection',
            name='dataset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.DataSet'),
        ),
        migrations.AddField(
            model_name='collection',
            name='metric',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Metric'),
        ),
    ]
