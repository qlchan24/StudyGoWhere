# Generated by Django 3.0.6 on 2020-05-17 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sgw', '0004_auto_20200516_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studyspot',
            name='openingTime',
            field=models.IntegerField(),
        ),
    ]
