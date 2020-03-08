# Generated by Django 3.0.4 on 2020-03-07 17:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('status', models.IntegerField(choices=[(1, 1), (2, 2)], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='StackComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(default='')),
                ('video', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=19)),
                ('at_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'Stack_Comment',
                'ordering': ['at_time'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Test', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(default='')),
                ('video', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=19)),
                ('at_time', models.DateTimeField(default=datetime.datetime.now)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='web.Post')),
            ],
            options={
                'ordering': ['at_time'],
                'abstract': False,
            },
        ),
    ]
