# Generated by Django 3.2.9 on 2021-11-27 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_student_sinit'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Sfname',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='الاسم الاول '),
        ),
        migrations.AddField(
            model_name='student',
            name='Slname',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='الجد'),
        ),
        migrations.AddField(
            model_name='student',
            name='Smname',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='الاب'),
        ),
    ]