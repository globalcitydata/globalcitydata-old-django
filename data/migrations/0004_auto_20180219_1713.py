# Generated by Django 2.0.1 on 2018-02-19 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20180217_0031'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='type',
            field=models.CharField(default='dataset', max_length=10),
        ),
        migrations.AddField(
            model_name='datasetmodel',
            name='type',
            field=models.CharField(default='model', max_length=10),
        ),
    ]
