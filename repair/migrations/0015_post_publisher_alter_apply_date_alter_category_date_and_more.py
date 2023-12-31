# Generated by Django 4.1.3 on 2022-12-11 07:54

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0014_remove_post_publisher_alter_apply_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='publisher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='repair.profile'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 11, 10, 54, 35, 458460)),
        ),
        migrations.AlterField(
            model_name='category',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 11, 10, 54, 35, 458460)),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 11, 10, 54, 35, 458460)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 11, 10, 54, 35, 458460)),
        ),
    ]
