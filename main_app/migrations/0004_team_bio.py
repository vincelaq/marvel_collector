# Generated by Django 3.2.7 on 2021-10-07 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='bio',
            field=models.TextField(default=None, max_length=500),
        ),
    ]
