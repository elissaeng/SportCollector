# Generated by Django 3.2.3 on 2021-05-27 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_sport_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='sport',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.sport'),
        ),
    ]
