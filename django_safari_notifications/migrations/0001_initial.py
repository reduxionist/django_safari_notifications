# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-12-11 07:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('website_push_id', models.CharField(max_length=255)),
                ('url_format_string', models.CharField(max_length=255)),
                ('web_service_url', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DomainNames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.URLField(db_index=True, max_length=255)),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='names', to='django_safari_notifications.Domain')),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', model_utils.fields.StatusField(choices=[('granted', 'granted'), ('denied', 'denied')], default='granted', max_length=100, no_check_for_status=True, verbose_name='status')),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='status', verbose_name='status changed')),
                ('token', models.CharField(max_length=180, unique=True)),
                ('website_push_id', models.CharField(default='', max_length=255)),
                ('domain', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tokens', to='django_safari_notifications.Domain')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
