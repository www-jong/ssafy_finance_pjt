# Generated by Django 4.2.4 on 2023-11-19 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="DepositProducts",
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
                ("fin_prdt_cd", models.TextField(unique=True)),
                ("kor_co_nm", models.TextField()),
                ("fin_prdt_nm", models.TextField()),
                ("etc_note", models.TextField(default="없음", null=True)),
                ("join_deny", models.IntegerField()),
                ("join_member", models.TextField(default="없음", null=True)),
                ("join_way", models.TextField(default="없음", null=True)),
                ("spcl_cnd", models.TextField(default="없음", null=True)),
            ],
        ),
        migrations.CreateModel(
            name="DepositOptions",
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
                ("fin_prdt_cd", models.TextField()),
                ("intr_rate_type_nm", models.CharField(max_length=100)),
                ("intr_rate", models.FloatField(default=-1, null=True)),
                ("intr_rate2", models.FloatField(default=-1, null=True)),
                ("save_trm", models.IntegerField()),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.depositproducts",
                    ),
                ),
            ],
        ),
    ]
