# Generated by Django 4.1 on 2023-09-29 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
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
                ("customer_first_name", models.CharField(max_length=100)),
                ("customer_last_name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Ips",
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
                ("address", models.GenericIPAddressField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("available", "available"),
                            ("allocated", "allocated"),
                            ("reserved", "reserved"),
                        ],
                        default="available",
                        max_length=20,
                    ),
                ),
                (
                    "customer",
                    models.OneToOneField(
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="ip.customer",
                    ),
                ),
            ],
        ),
    ]