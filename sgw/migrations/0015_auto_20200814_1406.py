# Generated by Django 3.0.6 on 2020-08-14 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sgw', '0014_auto_20200813_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='studyspot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='sgw.StudySpot'),
        ),
    ]