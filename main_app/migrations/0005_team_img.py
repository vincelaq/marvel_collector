# Generated by Django 3.2.7 on 2021-10-07 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_team_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='img',
            field=models.CharField(default=None, max_length=250),
        ),
    ]