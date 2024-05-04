# Generated by Django 5.0.3 on 2024-04-23 12:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("savvyfoods", "0013_cart_quantity"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="cart",
            name="image",
            field=models.ImageField(null=True, upload_to="foods"),
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("image", models.ImageField(null=True, upload_to="foods")),
                ("rating", models.IntegerField()),
                ("deliveryfee", models.IntegerField()),
                ("category", models.CharField(max_length=20)),
                ("price", models.IntegerField()),
                ("quantity", models.IntegerField(default=1)),
                ("delivered", models.BooleanField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]