# Generated by Django 4.1.5 on 2023-01-19 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("controle_pav", "0024_alter_esgoto_ss"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pendencias",
            name="Detalhes",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="pendencias",
            name="Solicitante",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="pendencias",
            name="Tipo",
            field=models.CharField(max_length=255),
        ),
    ]
