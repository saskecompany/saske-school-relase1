# Generated by Django 3.2.9 on 2021-12-15 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_catgory_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='catgory',
            options={'verbose_name': 'الفرع', 'verbose_name_plural': 'الفروع'},
        ),
    ]
