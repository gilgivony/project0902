# Generated by Django 2.0.3 on 2018-04-09 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fob', '0004_worker_report_user_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='worker_report',
            old_name='comment',
            new_name='user_comment',
        ),
        migrations.RenameField(
            model_name='worker_report',
            old_name='day',
            new_name='work_day',
        ),
    ]