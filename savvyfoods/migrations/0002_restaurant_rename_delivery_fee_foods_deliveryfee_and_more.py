# Generated by Django 5.0.3 on 2024-04-15 21:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("savvyfoods", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Restaurant",
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
                ("logo", models.ImageField(upload_to="retaurants_logos")),
            ],
        ),
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
        migrations.CreateModel(
            name="Cart",
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
                ("order", models.CharField(max_length=200)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Orders",
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
                ("address", models.CharField(max_length=100)),
                ("orders", models.TextField(max_length=100)),
                ("paid", models.BooleanField(default=False)),
                ("delivered", models.BooleanField(default=False)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="foods",
            name="restaurant",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="savvyfoods.restaurant",
            ),
        ),
    ]
