# Generated by Django 3.2.3 on 2021-05-24 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_api', '0002_studentmodel_validated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='rows',
            field=models.CharField(max_length=100000),
        ),
    ]
