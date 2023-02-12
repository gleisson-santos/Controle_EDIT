# Generated by Django 4.1.1 on 2023-02-11 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle_pav', '0051_alter_material_devolucao_alter_material_item_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='Executado',
            field=models.BooleanField(choices=[('Executado', 'Executado'), ('Pendente', 'Pendente')], default=False),
        ),
        migrations.AlterField(
            model_name='material',
            name='Localidade',
            field=models.TextField(choices=[('Salvador', 'Salvador'), ('Lauro', 'Lauro')], max_length=255),
        ),
        migrations.AlterField(
            model_name='material',
            name='Servico',
            field=models.CharField(choices=[('Operacional', 'Operacional'), ('Comercial', 'Comercial')], max_length=255),
        ),
    ]
