# Generated by Django 5.1.4 on 2025-01-09 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='release_year',
            field=models.PositiveIntegerField(default='0000'),
            preserve_default=False,
        ),
    ]
