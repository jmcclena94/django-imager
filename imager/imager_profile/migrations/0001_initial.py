# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-11 22:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('camera_type', models.CharField(max_length=255)),
                ('type_of_photography', models.CharField(choices=[('portrait', 'Portrait'), ('landscape', 'Landscape'), ('sports', 'Sports'), ('bw', 'Black and White'), ('nature', 'Nature')], max_length=128)),
                ('region', models.CharField(choices=[('pnw', 'Pacific Northwest'), ('ne', 'New England'), ('mdw', 'Midwest'), ('se', 'Southeast'), ('ma', 'Mid-Atlantic'), ('sw', 'Southwest'), ('mtw', 'Mountain West'), ('ca', 'California'), ('ak', 'Alaska'), ('hi', 'Hawaii')], max_length=3)),
                ('friends', models.ManyToManyField(related_name='friend_of', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
