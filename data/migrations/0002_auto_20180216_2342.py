# Generated by Django 2.0.1 on 2018-02-16 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='publish',
            field=models.BooleanField(choices=[(True, 'true'), (False, 'false')], default=True),
        ),
        migrations.AlterField(
            model_name='datasetmodel',
            name='publish',
            field=models.BooleanField(choices=[(True, 'true'), (False, 'false')], default=True),
        ),
    ]
