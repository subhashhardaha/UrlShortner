# Generated by Django 3.0.5 on 2020-05-17 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0002_clickevent_remote_add'),
    ]

    operations = [
        migrations.AddField(
            model_name='clickevent',
            name='http_referer',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='clickevent',
            name='http_user_agent',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
