# Generated by Django 4.1.6 on 2023-02-09 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mainmodel',
            old_name='primary_mobile',
            new_name='mobile',
        ),
        migrations.AlterField(
            model_name='mainmodel',
            name='notification_time',
            field=models.DateTimeField(db_index=True),
        ),
    ]