# Generated by Django 2.0.1 on 2018-02-14 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20180205_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='contact_details',
            field=models.EmailField(default='example@gmail.com', max_length=50),
        ),
    ]
