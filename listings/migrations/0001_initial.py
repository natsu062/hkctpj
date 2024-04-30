# Generated by Django 3.2 on 2024-04-30 04:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('sqrt', models.ImageField(upload_to='')),
                ('bathrooms', models.IntegerField()),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%M/%D')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%M/%D')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%M/%D')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%M/%D')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%Y/%M/%D')),
                ('photo_5', models.ImageField(blank=True, upload_to='photos/%Y/%M/%D')),
                ('photo_6', models.ImageField(blank=True, upload_to='photos/%Y/%M/%D')),
                ('is_published', models.BooleanField(default=True)),
                ('list_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.realtor')),
            ],
        ),
    ]
