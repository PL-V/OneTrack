# Generated by Django 5.0.6 on 2024-08-03 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mission',
            name='asset',
        ),
        migrations.AddField(
            model_name='mission',
            name='asset',
            field=models.ManyToManyField(to='home.asset'),
        ),
    ]