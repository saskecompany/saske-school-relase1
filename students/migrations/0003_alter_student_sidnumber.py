# Generated by Django 3.2.9 on 2021-11-25 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20211124_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Sidnumber',
            field=models.BigIntegerField(blank=True, max_length=14, null=True, verbose_name='الرقم القومي'),
        ),
    ]
