# Generated by Django 3.1.3 on 2021-07-21 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_auto_20210721_1312'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='enrollment_id',
            new_name='enrollment',
        ),
    ]
