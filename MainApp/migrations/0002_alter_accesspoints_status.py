# Generated by Django 4.2.3 on 2023-09-04 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesspoints',
            name='status',
            field=models.IntegerField(),
        ),
    ]