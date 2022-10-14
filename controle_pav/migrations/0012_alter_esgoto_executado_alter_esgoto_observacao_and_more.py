# Generated by Django 4.1.1 on 2022-09-21 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("controle_pav", "0011_pavimento_met_final_pavimento_ss_final"),
    ]

    operations = [
        migrations.AlterField(
            model_name="esgoto",
            name="Executado",
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name="esgoto",
            name="Observacao",
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="pavimento",
            name="Met_Final",
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="pavimento",
            name="Metragem",
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="pavimento",
            name="Observacao",
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="pavimento",
            name="Ss_Final",
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="pendencias",
            name="Solicitante",
            field=models.TextField(blank=True, max_length=255),
        ),
    ]
