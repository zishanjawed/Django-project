# Generated by Django 2.2.5 on 2020-02-10 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people_register', '0006_auto_20200210_0822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='city',
            field=models.ForeignKey(on_delete=None, to='people_register.City'),
        ),
    ]
