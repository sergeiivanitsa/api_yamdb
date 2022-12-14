# Generated by Django 2.2.16 on 2022-06-08 17:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0019_auto_20220608_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(db_index=True, max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name='title',
            name='name',
            field=models.TextField(db_index=True),
        ),
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.PositiveSmallIntegerField(db_index=True, validators=[django.core.validators.MaxValueValidator(2022)]),
        ),
    ]
