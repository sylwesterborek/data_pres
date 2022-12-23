# Generated by Django 3.2.14 on 2022-11-13 19:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_pres', '0002_auto_20221113_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dane',
            name='dana1',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxLengthValidator(8), django.core.validators.MinLengthValidator(0)]),
        ),
    ]