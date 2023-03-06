# Generated by Django 4.1.5 on 2023-03-06 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("controle_pav", "0010_alter_pavimento_bairro"),
    ]

    operations = [
        migrations.AlterField(
            model_name="esgoto",
            name="Bairro",
            field=models.CharField(
                choices=[
                    ("1 - Ipitinga", "1 - Ipitinga"),
                    ("2 - Vilas Atlantico", "2 - Vilas Atlantico"),
                    ("3 - Caji", "3 - Caji"),
                    ("4 - Areia Branca", "4 - Areia Branca"),
                    ("5 - Portao", "5 - Portao"),
                    ("6 - Vila Praiana", "6 - Vila Praiana"),
                    ("7 - Aracui", "7 - Aracui"),
                    ("8 - Jockey Clube", "8 - Jockey Clube"),
                    ("9 - Pitangueiras", "9 - Pitangueiras"),
                    ("10 - Centro", "10 - Centro"),
                    ("11 - Buraquinho", "11 - Buraquinho"),
                    ("13 - Itinga", "13 - Itinga"),
                    ("14 - Sao Cristovao", "14 - Sao Cristovao"),
                    ("15 - Cassange", "15 - Cassange"),
                    ("16 - Est do Coco", "16 - Est do Coco"),
                    ("17 - Jd Aeroporto", "17 - Jd Aeroporto"),
                    ("18 - Pa do Flamengo", "18 - Pa do Flamengo"),
                    ("19 - Jambeiro", "19 - Jambeiro"),
                    ("20 - Capelao SSA", "20 - Capelao SSA"),
                    ("21 - Lote Miragem", "21 - Lote Miragem"),
                    ("23 - Itinga SSA", "23 - Itinga SSA"),
                    ("24 - Ipitinga SSA", "24 - Ipitinga SSA"),
                    ("25 - Areia Branca SSA", "25 - Areia Branca SSA"),
                    ("26 - Cassange SSA", "26 - Cassange SSA"),
                    ("27 - Stella Maris SSA", "27 - Stella Maris SSA"),
                    ("28 - Aeroporto", "28 - Aeroporto"),
                    ("29 - Jd Castelao", "29 - Jd Castelao"),
                    ("31 - Quingoma", "31 - Quingoma"),
                    ("33 - Jd dos Passaros", "33 - Jd dos Passaros"),
                    ("34 - Cia Mar SSA", "34 - Cia Mar SSA"),
                    ("35 - Recrei Ipitinga", "35 - Recrei Ipitinga"),
                    ("36 - Caixa Dagua", "36 - Caixa Dagua"),
                    ("37 - Vida Nova", "37 - Vida Nova"),
                    ("38 - Capelao", "38 - Capelao"),
                    ("39 - Pq Sao Paulo", "39 - Pq Sao Paulo"),
                ],
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="materialbase",
            name="Equipe",
            field=models.CharField(
                blank=True,
                choices=[
                    ("1 - Ipitinga", "1 - Ipitinga"),
                    ("2 - Vilas Atlantico", "2 - Vilas Atlantico"),
                    ("3 - Caji", "3 - Caji"),
                    ("4 - Areia Branca", "4 - Areia Branca"),
                    ("5 - Portao", "5 - Portao"),
                    ("6 - Vila Praiana", "6 - Vila Praiana"),
                    ("7 - Aracui", "7 - Aracui"),
                    ("8 - Jockey Clube", "8 - Jockey Clube"),
                    ("9 - Pitangueiras", "9 - Pitangueiras"),
                    ("10 - Centro", "10 - Centro"),
                    ("11 - Buraquinho", "11 - Buraquinho"),
                    ("13 - Itinga", "13 - Itinga"),
                    ("14 - Sao Cristovao", "14 - Sao Cristovao"),
                    ("15 - Cassange", "15 - Cassange"),
                    ("16 - Est do Coco", "16 - Est do Coco"),
                    ("17 - Jd Aeroporto", "17 - Jd Aeroporto"),
                    ("18 - Pa do Flamengo", "18 - Pa do Flamengo"),
                    ("19 - Jambeiro", "19 - Jambeiro"),
                    ("20 - Capelao SSA", "20 - Capelao SSA"),
                    ("21 - Lote Miragem", "21 - Lote Miragem"),
                    ("23 - Itinga SSA", "23 - Itinga SSA"),
                    ("24 - Ipitinga SSA", "24 - Ipitinga SSA"),
                    ("25 - Areia Branca SSA", "25 - Areia Branca SSA"),
                    ("26 - Cassange SSA", "26 - Cassange SSA"),
                    ("27 - Stella Maris SSA", "27 - Stella Maris SSA"),
                    ("28 - Aeroporto", "28 - Aeroporto"),
                    ("29 - Jd Castelao", "29 - Jd Castelao"),
                    ("31 - Quingoma", "31 - Quingoma"),
                    ("33 - Jd dos Passaros", "33 - Jd dos Passaros"),
                    ("34 - Cia Mar SSA", "34 - Cia Mar SSA"),
                    ("35 - Recrei Ipitinga", "35 - Recrei Ipitinga"),
                    ("36 - Caixa Dagua", "36 - Caixa Dagua"),
                    ("37 - Vida Nova", "37 - Vida Nova"),
                    ("38 - Capelao", "38 - Capelao"),
                    ("39 - Pq Sao Paulo", "39 - Pq Sao Paulo"),
                ],
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="pavimento",
            name="Bairro",
            field=models.CharField(
                blank=True,
                choices=[
                    ("1 - Ipitinga", "1 - Ipitinga"),
                    ("2 - Vilas Atlantico", "2 - Vilas Atlantico"),
                    ("3 - Caji", "3 - Caji"),
                    ("4 - Areia Branca", "4 - Areia Branca"),
                    ("5 - Portao", "5 - Portao"),
                    ("6 - Vila Praiana", "6 - Vila Praiana"),
                    ("7 - Aracui", "7 - Aracui"),
                    ("8 - Jockey Clube", "8 - Jockey Clube"),
                    ("9 - Pitangueiras", "9 - Pitangueiras"),
                    ("10 - Centro", "10 - Centro"),
                    ("11 - Buraquinho", "11 - Buraquinho"),
                    ("13 - Itinga", "13 - Itinga"),
                    ("14 - Sao Cristovao", "14 - Sao Cristovao"),
                    ("15 - Cassange", "15 - Cassange"),
                    ("16 - Est do Coco", "16 - Est do Coco"),
                    ("17 - Jd Aeroporto", "17 - Jd Aeroporto"),
                    ("18 - Pa do Flamengo", "18 - Pa do Flamengo"),
                    ("19 - Jambeiro", "19 - Jambeiro"),
                    ("20 - Capelao SSA", "20 - Capelao SSA"),
                    ("21 - Lote Miragem", "21 - Lote Miragem"),
                    ("23 - Itinga SSA", "23 - Itinga SSA"),
                    ("24 - Ipitinga SSA", "24 - Ipitinga SSA"),
                    ("25 - Areia Branca SSA", "25 - Areia Branca SSA"),
                    ("26 - Cassange SSA", "26 - Cassange SSA"),
                    ("27 - Stella Maris SSA", "27 - Stella Maris SSA"),
                    ("28 - Aeroporto", "28 - Aeroporto"),
                    ("29 - Jd Castelao", "29 - Jd Castelao"),
                    ("31 - Quingoma", "31 - Quingoma"),
                    ("33 - Jd dos Passaros", "33 - Jd dos Passaros"),
                    ("34 - Cia Mar SSA", "34 - Cia Mar SSA"),
                    ("35 - Recrei Ipitinga", "35 - Recrei Ipitinga"),
                    ("36 - Caixa Dagua", "36 - Caixa Dagua"),
                    ("37 - Vida Nova", "37 - Vida Nova"),
                    ("38 - Capelao", "38 - Capelao"),
                    ("39 - Pq Sao Paulo", "39 - Pq Sao Paulo"),
                ],
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="pavimento",
            name="Equipe",
            field=models.CharField(
                blank=True,
                choices=[
                    ("106-A - JOSEILTON SANTOS", "106-A - JOSEILTON SANTOS"),
                    (
                        "111-A - VANILTON DA SILVA DE JESUS",
                        "111-A - VANILTON DA SILVA DE JESUS",
                    ),
                    (
                        "126-A - LUIZ ANTONIO SANTOS RAMOS",
                        "126-A - LUIZ ANTONIO SANTOS RAMOS",
                    ),
                    ("127-A - GENILSON LIMA VITORIA", "127-A - GENILSON LIMA VITORIA"),
                    (
                        "132A - MARCOS CASSIO DE JESUS SILVA",
                        "132A - MARCOS CASSIO DE JESUS SILVA",
                    ),
                    (
                        "144-A - EDILSON PETRONILIO DA SILVA",
                        "144-A - EDILSON PETRONILIO DA SILVA",
                    ),
                    (
                        "210A - JOSEILTON JESUS DOS SANTOS",
                        "210A - JOSEILTON JESUS DOS SANTOS",
                    ),
                    ("213A - SILVIO ALVES DA HORA", "213A - SILVIO ALVES DA HORA"),
                    (
                        "214-A - CRISTIANO VIANA MACEDO",
                        "214-A - CRISTIANO VIANA MACEDO",
                    ),
                    (
                        "215-A - NARCISO CONCEICAO FRANCA",
                        "215-A - NARCISO CONCEICAO FRANCA",
                    ),
                    (
                        "218A - JILTON RENILTON DE MELO",
                        "218A - JILTON RENILTON DE MELO",
                    ),
                    (
                        "221-A - EDCARLOS CARVALHO ALMEIDA",
                        "221-A - EDCARLOS CARVALHO ALMEIDA",
                    ),
                    (
                        "221-E - EDMILSON GOLVEIA ALMEIDA",
                        "221-E - EDMILSON GOLVEIA ALMEIDA",
                    ),
                    (
                        "222-A - EDVALDO RAIMUNDO DOS SANTOS",
                        "222-A - EDVALDO RAIMUNDO DOS SANTOS",
                    ),
                    (
                        "222E - GILVANDO DE SOUZA SANTOS",
                        "222E - GILVANDO DE SOUZA SANTOS",
                    ),
                    (
                        "308A - ADAILTON PASSOS DE SOUZA",
                        "308A - ADAILTON PASSOS DE SOUZA",
                    ),
                    ("309A - JOSE ROBERIO RODRIGUES", "309A - JOSE ROBERIO RODRIGUES"),
                    (
                        "310A - MARCOS JOSE CORREIA DOS SANTOS",
                        "310A - MARCOS JOSE CORREIA DOS SANTOS",
                    ),
                    (
                        "311-E - ADILTON JOSE DA SILVA SANTOS",
                        "311-E - ADILTON JOSE DA SILVA SANTOS",
                    ),
                    ("315-A - HANILTON SANTOS LOPES", "315-A - HANILTON SANTOS LOPES"),
                    ("320A - CELIO ROBERTO DE JESUS", "320A - CELIO ROBERTO DE JESUS"),
                    (
                        "402-E - CARLOS ALBERIO DOS SANTOS",
                        "402-E - CARLOS ALBERIO DOS SANTOS",
                    ),
                    ("405-E - MANOEL JOSE", "405-E - MANOEL JOSE"),
                    (
                        "409E - ULISSES ALVES DOS SANTOS FILHO",
                        "409E - ULISSES ALVES DOS SANTOS FILHO",
                    ),
                    ("410E - JOSE TELES FILHO", "410E - JOSE TELES FILHO"),
                    (
                        "422-E - REGINALDO FERREIRA SANTOS",
                        "422-E - REGINALDO FERREIRA SANTOS",
                    ),
                    (
                        "ASF700 - JOSEVAL NATIVIDADE DE JESUS",
                        "ASF700 - JOSEVAL NATIVIDADE DE JESUS",
                    ),
                    (
                        "CARLF - SERVICOS DE CARRO AGUA",
                        "CARLF - SERVICOS DE CARRO AGUA",
                    ),
                    ("ENC-07 - REGINALDO DA SILVA", "ENC-07 - REGINALDO DA SILVA"),
                    (
                        "PAV04A - VALDNEI VIEIRA DA CRUZ",
                        "PAV04A - VALDNEI VIEIRA DA CRUZ",
                    ),
                    (
                        "PAV09 - AILTON DE JESUS TEIXEIRA",
                        "PAV09 - AILTON DE JESUS TEIXEIRA",
                    ),
                    ("PG AG1 - PROGAGUA01", "PG AG1 - PROGAGUA01"),
                    ("PG ES1 - PROGESGOTO01", "PG ES1 - PROGESGOTO01"),
                    ("PVASF - PAVASFALTO", "PVASF - PAVASFALTO"),
                    (
                        "307-E - AILTON DOS SANTOS MACHADO",
                        "307-E - AILTON DOS SANTOS MACHADO",
                    ),
                    ("301-E - AMILTON BISPO DA CRUZ", "301-E - AMILTON BISPO DA CRUZ"),
                ],
                max_length=255,
            ),
        ),
    ]
