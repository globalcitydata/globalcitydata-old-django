# Generated by Django 2.0.1 on 2018-02-17 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20180217_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='publish',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='datasetmodel',
            name='publish',
            field=models.BooleanField(default=True),
        ),
    ]
