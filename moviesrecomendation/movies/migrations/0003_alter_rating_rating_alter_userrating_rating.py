# Generated by Django 4.2.10 on 2024-05-08 11:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_rating_rating_alter_userrating_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.FloatField(validators=[django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='userrating',
            name='rating',
            field=models.FloatField(validators=[django.core.validators.MaxValueValidator(10)]),
        ),
    ]