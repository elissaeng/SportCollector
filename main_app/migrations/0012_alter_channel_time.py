# Generated by Django 3.2.3 on 2021-06-02 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_auto_20210531_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='time',
            field=models.TextField(max_length=15),
        ),
    ]
