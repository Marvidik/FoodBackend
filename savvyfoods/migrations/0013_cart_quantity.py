# Generated by Django 5.0.3 on 2024-04-22 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("savvyfoods", "0012_remove_cart_contents"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="quantity",
            field=models.IntegerField(default=1),
        ),
    ]