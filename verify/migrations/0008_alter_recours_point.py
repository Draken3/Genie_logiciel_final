# Generated by Django 4.0 on 2023-04-26 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verify', '0007_rename_cotes_recours_point'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recours',
            name='point',
            field=models.IntegerField(default=0),
        ),
    ]