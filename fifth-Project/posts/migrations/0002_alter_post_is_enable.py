# Generated by Django 4.2.3 on 2023-07-11 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='is_enable',
            field=models.BooleanField(default=True),
        ),
    ]
