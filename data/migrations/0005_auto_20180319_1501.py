# Generated by Django 2.0.1 on 2018-03-19 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_auto_20180223_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='FuturesModeling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, choices=[('Historical Data', 'Historical Data'), ('Base Year Data', 'Base Year Data'), ('Futures Modeling Data', 'Futures Modeling Data')], default='', max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, choices=[('One Time Assessment', 'One Time Assessment'), ('Time Series', 'Time Series')], default='', max_length=10, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='dataset',
            name='futures_modeling',
            field=models.ManyToManyField(to='data.FuturesModeling'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='time',
            field=models.ManyToManyField(to='data.Time'),
        ),
    ]
