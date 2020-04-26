# Generated by Django 2.2.7 on 2020-04-26 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_product_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='description',
            new_name='active_substance',
        ),
        migrations.AddField(
            model_name='product',
            name='dosage_form',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='manufacturer',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='pharmachologic_effect',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]