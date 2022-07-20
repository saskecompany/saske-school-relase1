# Generated by Django 3.2.9 on 2021-12-08 01:32

from django.db import migrations, models
import django.db.models.deletion
import tasks.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0003_auto_20211129_0756'),
    ]

    operations = [
        migrations.CreateModel(
            name='exams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='عنوان الامتحان')),
                ('publishAt', models.DateTimeField(auto_now=True, verbose_name='التاريخ')),
            ],
        ),
        migrations.CreateModel(
            name='task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quest', models.TextField(verbose_name='السؤال')),
                ('questimg', models.ImageField(blank=True, null=True, upload_to=tasks.models.task.askimgupload, verbose_name='صورة السؤال')),
                ('answer1', models.CharField(blank=True, max_length=50, null=True, verbose_name='الاجابه الاولي')),
                ('answer2', models.CharField(blank=True, max_length=50, null=True, verbose_name='الاجابه الثانيه')),
                ('answer3', models.CharField(blank=True, max_length=50, null=True, verbose_name='الاجابه الثالثه')),
                ('answer4', models.CharField(blank=True, max_length=50, null=True, verbose_name='الاجابه الرابعه')),
                ('answer', models.CharField(blank=True, choices=[('1', 'الاجابه الاولي'), ('2', 'الاجابه الثانيه'), ('3', 'الاجابه الثالثه'), ('4', 'الاجابه الرابعه')], max_length=50, null=True, verbose_name='الاجابه الصحيحه')),
                ('lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.lessons', verbose_name='الدرس المتعلق')),
            ],
        ),
    ]
