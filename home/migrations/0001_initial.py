# Generated by Django 3.2.9 on 2021-11-23 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='اسم الحصه')),
                ('date', models.DateField(auto_now_add=True, verbose_name='تاريخ الحصه')),
                ('isfinished', models.BooleanField(max_length=256, verbose_name='انتهت')),
                ('video', models.FileField(upload_to=None, verbose_name='الحصه')),
            ],
        ),
    ]