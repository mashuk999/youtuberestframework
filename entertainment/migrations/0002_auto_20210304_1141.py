# Generated by Django 3.1.7 on 2021-03-04 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entertainment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entertainmentdb',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]
