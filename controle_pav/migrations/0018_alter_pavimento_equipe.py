# Generated by Django 4.1.1 on 2022-11-06 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle_pav', '0017_alter_pavimento_equipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pavimento',
            name='Equipe',
            field=models.TextField(choices=[('equipes', 'Equipe1'), ('equipes', 'Equipe2'), ('equipes', 'Equipe3'), ('equipes', 'Equipe5')], max_length=255),
        ),
    ]
