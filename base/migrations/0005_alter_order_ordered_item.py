# Generated by Django 3.2.8 on 2021-10-31 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_vendor_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ordered_item',
            field=models.JSONField(),
        ),
    ]
