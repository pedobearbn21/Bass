# Generated by Django 3.0.3 on 2020-03-03 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20200303_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=19),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='video',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='stackcomment',
            name='price',
            field=models.DecimalField(decimal_places=2, default=10, max_digits=19),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stackcomment',
            name='video',
            field=models.TextField(blank=True),
        ),
    ]