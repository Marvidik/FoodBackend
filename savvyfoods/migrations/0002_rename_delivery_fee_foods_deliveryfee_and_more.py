# Generated by Django 5.0.3 on 2024-04-04 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("savvyfoods", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="foods",
            old_name="delivery_fee",
            new_name="deliveryfee",
        ),
        migrations.RenameField(
            model_name="foods",
            old_name="delivery_time",
            new_name="deliverytime",
        ),
        migrations.RenameField(
            model_name="foods",
            old_name="fast_food",
            new_name="fastfood",
        ),
        migrations.RenameField(
            model_name="junks",
            old_name="delivery_fee",
            new_name="deliveryfee",
        ),
        migrations.RenameField(
            model_name="junks",
            old_name="delivery_time",
            new_name="deliverytime",
        ),
        migrations.RenameField(
            model_name="junks",
            old_name="junk_name",
            new_name="junk",
        ),
    ]
