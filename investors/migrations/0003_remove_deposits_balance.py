# Generated by Django 4.1.5 on 2023-01-28 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('investors', '0002_deposits'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deposits',
            name='balance',
        ),
    ]
