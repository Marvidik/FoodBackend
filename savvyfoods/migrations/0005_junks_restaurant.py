# Generated by Django 5.0.3 on 2024-04-20 20:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("savvyfoods", "0004_rename_description_foods_availability_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="junks",
            name="restaurant",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="savvyfoods.restaurant",
            ),
        ),
    ]
