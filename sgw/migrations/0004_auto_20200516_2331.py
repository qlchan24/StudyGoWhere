# Generated by Django 3.0.6 on 2020-05-16 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sgw', '0003_studyspot_openingtime'),
    ]

    operations = [
        migrations.AddField(
            model_name='studyspot',
            name='airConditioned',
            field=models.BooleanField(
                choices=[(True, 'Yes'), (False, 'No')], default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studyspot',
            name='description',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studyspot',
            name='discussionFriendly',
            field=models.BooleanField(
                choices=[(True, 'Yes'), (False, 'No')], default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studyspot',
            name='wallSockets',
            field=models.BooleanField(
                choices=[(True, 'Yes'), (False, 'No')], default=False),
            preserve_default=False,
        ),
    ]
