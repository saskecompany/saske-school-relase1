# Generated by Django 3.2.9 on 2021-12-09 10:13

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0003_auto_20211129_0756'),
        ('reports', '0008_auto_20211209_0944'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='examReport',
            new_name='homeworkReport',
        ),
    ]
