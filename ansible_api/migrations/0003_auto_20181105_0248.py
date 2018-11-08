# Generated by Django 2.1.2 on 2018-11-05 02:48

import common.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ansible_api', '0002_auto_20181105_0227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playbookexecution',
            name='date_finished',
        ),
        migrations.RemoveField(
            model_name='playbookexecution',
            name='is_finished',
        ),
        migrations.RemoveField(
            model_name='playbookexecution',
            name='is_success',
        ),
        migrations.RemoveField(
            model_name='playbookexecution',
            name='raw',
        ),
        migrations.RemoveField(
            model_name='playbookexecution',
            name='summary',
        ),
        migrations.AddField(
            model_name='playbookexecution',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Create time'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='playbookexecution',
            name='date_end',
            field=models.DateTimeField(null=True, verbose_name='End time'),
        ),
        migrations.AddField(
            model_name='playbookexecution',
            name='result',
            field=common.models.JsonDictTextField(blank=True, default='{}', null=True, verbose_name='Result'),
        ),
        migrations.AddField(
            model_name='playbookexecution',
            name='state',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('STARTED', 'Started'), ('SUCCESS', 'Success'), ('FAILURE', 'Failure'), ('RETRY', 'Retry')], default='PENDING', max_length=16),
        ),
        migrations.AlterField(
            model_name='playbookexecution',
            name='date_start',
            field=models.DateTimeField(null=True, verbose_name='Start time'),
        ),
    ]