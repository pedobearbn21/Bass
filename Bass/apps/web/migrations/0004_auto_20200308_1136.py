# Generated by Django 3.0.4 on 2020-03-08 04:36

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0003_auto_20200308_1118'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Paymentss',
            new_name='Payment',
        ),
    ]