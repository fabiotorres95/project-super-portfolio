# Generated by Django 4.2.3 on 2023-12-07 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0002_project"),
    ]

    operations = [
        migrations.CreateModel(
            name="CertifyingInstitute",
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
                ("url", models.URLField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name="Certificate",
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
                ("timestamp", models.DateField(auto_now_add=True)),
                (
                    "certifying_institution",
                    models.ForeignKey(
                        max_length=500,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="projects.certifyinginstitute",
                    ),
                ),
                (
                    "profiles",
                    models.ManyToManyField(
                        max_length=500,
                        related_name="certificates",
                        to="projects.profile",
                    ),
                ),
            ],
        ),
    ]
