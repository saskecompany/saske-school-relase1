# Generated by Django 3.2.9 on 2021-12-12 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0013_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='homerport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.homeworkreport', verbose_name='واجبات الطالب'),
        ),
    ]
