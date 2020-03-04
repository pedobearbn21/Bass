# Generated by Django 3.0.3 on 2020-03-04 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_auto_20200303_1727'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stackcomment',
            name='post',
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='web.Post'),
        ),
    ]
