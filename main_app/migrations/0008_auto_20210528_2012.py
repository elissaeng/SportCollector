# Generated by Django 3.2.3 on 2021-05-28 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20210528_1856'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sport',
            name='sponsers',
        ),
        migrations.AddField(
            model_name='athlete',
            name='sponsers',
            field=models.ManyToManyField(blank=True, to='main_app.Sponser'),
        ),
    ]
