# Generated by Django 4.1.3 on 2022-12-11 07:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0013_alter_apply_date_alter_category_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='publisher',
        ),
        migrations.AlterField(
            model_name='apply',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 11, 10, 52, 25, 653859)),
        ),
        migrations.AlterField(
            model_name='category',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 11, 10, 52, 25, 653859)),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 11, 10, 52, 25, 638236)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 11, 10, 52, 25, 653859)),
        ),
    ]
