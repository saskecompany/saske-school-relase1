# Generated by Django 3.2.9 on 2021-12-09 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0003_auto_20211129_0756'),
    ]

    operations = [
        migrations.CreateModel(
            name='examReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asknumber', models.IntegerField(verbose_name='')),
                ('correctAnswers', models.IntegerField(verbose_name='')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.lessons', verbose_name='')),
            ],
        ),
    ]
