# Generated by Django 4.1.3 on 2022-12-14 15:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0028_alter_apply_date_alter_category_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 14, 18, 2, 32, 297015)),
        ),
        migrations.AlterField(
            model_name='category',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 14, 18, 2, 32, 297015)),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 14, 18, 2, 32, 295015)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 14, 18, 2, 32, 298015)),
        ),
    ]
