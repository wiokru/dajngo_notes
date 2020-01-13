# Generated by Django 2.2.7 on 2020-01-12 13:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Note', '0003_auto_20200112_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
