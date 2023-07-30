# Generated by Django 4.1.3 on 2022-12-10 11:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='country',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 10, 14, 10, 35, 649220)),
        ),
    ]