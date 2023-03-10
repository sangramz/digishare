# Generated by Django 4.1.5 on 2023-01-27 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('investors', '0001_initial'),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Investments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('investDate', models.DateTimeField(auto_now_add=True)),
                ('propInvested', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.investmentplans')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='investors.profile')),
            ],
        ),
    ]
