# Generated by Django 3.1.7 on 2021-03-04 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entertainment', '0004_auto_20210304_1815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entertainmentdb',
            name='date',
        ),
    ]
