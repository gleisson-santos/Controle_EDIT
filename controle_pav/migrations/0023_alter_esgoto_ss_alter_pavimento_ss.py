# Generated by Django 4.1.5 on 2023-01-19 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("controle_pav", "0022_alter_esgoto_ss"),
    ]

    operations = [
        migrations.AlterField(
            model_name="esgoto", name="Ss", field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="pavimento", name="Ss", field=models.CharField(max_length=9),
        ),
    ]