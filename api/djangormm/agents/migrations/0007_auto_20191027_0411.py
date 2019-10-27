# Generated by Django 2.2.6 on 2019-10-27 04:11

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0006_agent_ping_check_interval'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='cpu_info',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='disks',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='local_ip',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='logged_in_username',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='operating_system',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='public_ip',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='services',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
    ]
