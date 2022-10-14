# Generated by Django 4.1 on 2022-09-14 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("controle_pav", "0008_pavimento_prazo"),
    ]

    operations = [
        migrations.CreateModel(
            name="Pendencias",
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
                ("Tipo", models.TextField(max_length=255)),
                ("Solicitante", models.TextField(max_length=255)),
                ("Data", models.DateField(blank=True, null=True, verbose_name="data")),
                ("Detalhes", models.TextField(max_length=255)),
            ],
        ),
    ]
