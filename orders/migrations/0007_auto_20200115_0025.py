# Generated by Django 2.2.7 on 2020-01-14 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_productinbasket_session_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinbasket',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]