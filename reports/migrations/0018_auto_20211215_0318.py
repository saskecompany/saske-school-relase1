# Generated by Django 3.2.9 on 2021-12-15 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0017_auto_20211213_1540'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='examreport',
            options={'verbose_name': 'تقرير الامتحان', 'verbose_name_plural': 'تقارير الامتحانات'},
        ),
        migrations.AlterModelOptions(
            name='homeworkreport',
            options={'verbose_name': 'تفرير الواجب', 'verbose_name_plural': 'تقاربر الواجب'},
        ),
        migrations.AlterModelOptions(
            name='report',
            options={'verbose_name': 'التفرير', 'verbose_name_plural': 'التقارير'},
        ),
    ]
