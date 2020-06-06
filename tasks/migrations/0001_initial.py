# Generated by Django 2.2 on 2020-06-06 09:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=58)),
                ('description', models.TextField(blank=True, default='', max_length=200)),
                ('priority', models.IntegerField(default=3)),
                ('is_completed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]