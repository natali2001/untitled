# Generated by Django 2.2.7 on 2020-01-29 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinorder',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
