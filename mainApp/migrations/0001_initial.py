# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 21:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Path', models.CharField(max_length=100)),
                ('Title', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='tag',
            name='Video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.Video'),
        ),
    ]
