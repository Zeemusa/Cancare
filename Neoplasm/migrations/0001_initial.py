# Generated by Django 5.1.1 on 2024-12-12 20:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cancer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_cancer', models.CharField(max_length=35)),
                ('description', models.CharField(max_length=3000)),
                ('symptoms', models.CharField(max_length=5000)),
                ('treatment', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg_description', models.CharField(max_length=5000)),
                ('period', models.IntegerField(max_length=20)),
                ('date', models.DateTimeField(default=datetime.datetime.today)),
            ],
        ),
    ]
