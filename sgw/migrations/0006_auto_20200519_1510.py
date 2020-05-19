# Generated by Django 3.0.6 on 2020-05-19 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sgw', '0005_auto_20200517_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studyspot',
            name='airConditioned',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='studyspot',
            name='closingTime',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='studyspot',
            name='discussionFriendly',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='studyspot',
            name='openingTime',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='studyspot',
            name='wallSockets',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crowdedness', models.IntegerField()),
                ('whenRated', models.DateTimeField(auto_now_add=True)),
                ('studyspot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sgw.StudySpot')),
            ],
        ),
    ]
