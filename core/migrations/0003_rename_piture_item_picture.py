# Generated by Django 4.1.5 on 2023-01-19 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_category_item_price_item_category"),
    ]

    operations = [
        migrations.RenameField(
            model_name="item",
            old_name="piture",
            new_name="picture",
        ),
    ]
