# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-29 22:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producer', models.CharField(max_length=64)),
                ('car_model', models.CharField(max_length=64)),
                ('car_type', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='NewCarModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_num', models.CharField(max_length=32)),
                ('max_seats', models.IntegerField()),
                ('year', models.IntegerField()),
                ('car_class', models.CharField(choices=[('economy class', 'economy class'), ('business class', 'business class'), ('first class', 'first class')], max_length=32)),
                ('hybrid_or_electric', models.CharField(choices=[('Hybrid', 'Hybrid'), ('Electric', 'Electric'), ('None', 'None')], max_length=32)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car', to='fleet.CarsModel')),
            ],
        ),
    ]