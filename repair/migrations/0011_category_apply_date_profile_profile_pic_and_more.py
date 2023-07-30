# Generated by Django 4.1.3 on 2022-12-11 07:42

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('repair', '0010_apply_alter_order_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('disc', models.TextField(blank=True, max_length=300, null=True)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 11, 10, 42, 57, 779486))),
            ],
        ),
        migrations.AddField(
            model_name='apply',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 11, 10, 42, 57, 779486)),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 11, 10, 42, 57, 779486)),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(blank=True, choices=[('one', 'one'), ('two', 'two'), ('three', 'three'), ('four', 'four'), ('five', 'five')], max_length=255, null=True)),
                ('profile', models.ImageField(blank=True, upload_to='upload/blog')),
                ('one_topic', models.CharField(blank=True, max_length=255, null=True)),
                ('one_p1', models.TextField(blank=True, max_length=2555, null=True)),
                ('one_p2', models.TextField(blank=True, max_length=2555, null=True)),
                ('one_p3', models.TextField(blank=True, max_length=2555, null=True)),
                ('one_p4', models.TextField(blank=True, max_length=2555, null=True)),
                ('profile_two', models.ImageField(blank=True, upload_to='upload/blog')),
                ('two_topic', models.CharField(blank=True, max_length=255, null=True)),
                ('two_p1', models.TextField(blank=True, max_length=2555, null=True)),
                ('two_p2', models.TextField(blank=True, max_length=2555, null=True)),
                ('two_p3', models.TextField(blank=True, max_length=2555, null=True)),
                ('profile_three', models.ImageField(blank=True, upload_to='upload/blog')),
                ('three_topic', models.CharField(blank=True, max_length=255, null=True)),
                ('three_p1', models.TextField(blank=True, max_length=2555, null=True)),
                ('three_p2', models.TextField(blank=True, max_length=2555, null=True)),
                ('three_p3', models.TextField(blank=True, max_length=2555, null=True)),
                ('profile_four', models.ImageField(blank=True, upload_to='upload/blog')),
                ('four_topic', models.CharField(blank=True, max_length=255, null=True)),
                ('four_p1', models.TextField(blank=True, max_length=2555, null=True)),
                ('four_p2', models.TextField(blank=True, max_length=2555, null=True)),
                ('four_p3', models.TextField(blank=True, max_length=2555, null=True)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 11, 10, 42, 57, 779486))),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repair.category')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]