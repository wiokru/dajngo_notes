# Generated by Django 2.2.7 on 2020-01-12 12:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Note', '0002_auto_20200112_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='note',
            name='modified_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
