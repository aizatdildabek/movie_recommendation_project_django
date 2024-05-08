# Generated by Django 4.2.10 on 2024-05-05 08:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.FloatField(validators=[django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='userrating',
            name='rating',
            field=models.FloatField(validators=[django.core.validators.MaxValueValidator(5)]),
        ),
    ]