# Generated by Django 4.0 on 2023-04-06 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verify', '0002_rename_grade_cotes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotes',
            name='cote',
            field=models.IntegerField(default=0),
        ),
    ]
