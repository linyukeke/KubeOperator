# Generated by Django 2.1.2 on 2019-06-17 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openshift_api', '0030_auto_20190611_0909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deployexecution',
            name='extra_vars',
        ),
    ]