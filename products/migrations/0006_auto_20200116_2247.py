# Generated by Django 2.2.7 on 2020-01-16 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20191217_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='is_main',
            field=models.BooleanField(default=True),
        ),
    ]