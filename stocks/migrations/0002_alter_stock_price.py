# Generated by Django 5.1.7 on 2025-05-28 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='price',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
