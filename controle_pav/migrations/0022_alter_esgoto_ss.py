# Generated by Django 4.1.5 on 2023-01-19 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("controle_pav", "0021_alter_esgoto_bairro_alter_esgoto_equipe_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="esgoto", name="Ss", field=models.IntegerField(max_length=255),
        ),
    ]