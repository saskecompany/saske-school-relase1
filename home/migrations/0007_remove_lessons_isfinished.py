# Generated by Django 3.2.9 on 2022-07-19 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_catgory_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lessons',
            name='isfinished',
        ),
    ]
