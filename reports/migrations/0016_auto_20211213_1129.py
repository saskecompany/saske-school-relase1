# Generated by Django 3.2.9 on 2021-12-13 11:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0003_rename_exams_exam'),
        ('reports', '0015_auto_20211212_0210'),
    ]

    operations = [
        migrations.CreateModel(
            name='examReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asknumber', models.IntegerField(blank=True, null=True, verbose_name='عدد الاسئله')),
                ('correctAnswers', models.IntegerField(blank=True, null=True, verbose_name='الاجابات الصحيحه')),
                ('wrongAnswers', models.IntegerField(blank=True, null=True, verbose_name='الإجابات الخاطئه')),
                ('presentage', models.IntegerField(blank=True, null=True, verbose_name='النسبه المئويه')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.exam', verbose_name='واجب درس')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='الطالب')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='report',
            name='examReport',
            field=models.ManyToManyField(to='reports.examReport', verbose_name='امتحانات الطالب'),
        ),
    ]
