import csv
from datetime import date, datetime
from random import choices
from django.db import models
import pandas as pd
from django.contrib.auth.models import User




# df = pd.read_csv("C:/Users/55719/Desktop/#Projeto - Controle_servcio_EDIT/Controle_EDIT/controle_pav/static/texto/equipes.csv", header=None)
# print(df)

def Equipe():
    with open("controle_pav/static/texto/equipes.csv", 'r') as arquivo:
        equipes = arquivo.read().split()
        EQUIPE = tuple(('equipes', equipes[i]) for i in range(len(equipes)))
    return EQUIPE

# modelos que irão representar uma tabela no banco de dados
class Pavimento(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    last_edited_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+', editable=False)
     
    Ss = models.CharField(max_length=9)
    Data = models.DateField('data', null=True, blank=True)
    Prazo = models.BooleanField(default=False)
         

    Equipe = models.CharField(max_length=255, choices=Equipe())
    
    BAIRRO = [ ('Ipitanga', 'Ipitanga'), ('Vilas Atlântico', 'Vilas Atlântico'), ('Caji', 'Caji'), ('Areia Branca', 'Areia Branca'), ('Portao', 'Portão'), ('Vila Praiana', 'Vila Praiana'), ('Aracui', 'Aracui'), ('Jockey Clube', 'Jockey Clube'), ('Pitangueiras', 'Pitangueiras'), ('Centro', 'Centro'), ('Buraquinho', 'Buraquinho'), ('Castanheiras', 'Castanheiras'), ('Itinga', 'Itinga'), ('São Cristóvão', 'São Cristóvão'), ('Cassange', 'Cassange'), ('"Est do Coco', 'Est do Coco'), ('Jd Aeroporto', 'Jd Aeroporto'), ('Pa do Flamengo', 'Pa do Flamengo'), ('Jambeiro', 'Jambeiro'), ('Capelao SSA', 'Capelão SSA'), ('Lot Miragem', 'Lot Miragem'), ('Jd Margaridas', 'Jd Margaridas'), ('Itinga SSA', 'Itinga SSA'), ('Ipitanga SSA', 'Ipitanga SSA'), ('Areia Branc SSA', 'Areia Branc SSA'), ]
    Bairro = models.CharField(max_length=255, choices=BAIRRO)
    Rua = models.CharField(max_length=255)
    Referencia = models.CharField(max_length=255)

    SERVICO = (
        ("Asfalto", "Asfalto"),
        ("Concreto", "Concreto"),
        ("Blocos", "Blocos")
    )

    Servico = models.CharField(max_length=255, choices=SERVICO, verbose_name=("Serviço"))

    Metragem = models.CharField(max_length=255)
    Observacao = models.CharField(max_length=255, blank=True)
    Ss_Final = models.CharField(max_length=255, blank=True)
    Met_Final = models.CharField(max_length=255, blank=True)

    EXECUTADO = (
        (True, "Executado"),
        (False, "Pendente")
    )

    Executado = models.BooleanField(default=False, choices=EXECUTADO, db_index=True)

    LOCALIDADE = (
        ('Salvador', "Salvador"),
        ('Lauro', "Lauro")
    )
    Localidade = models.TextField(max_length=255, choices=LOCALIDADE, db_index=True)

    MEDIR = (
        ('Medir', "Medir"),
        ('Normal', "Normal"),
        ('Prioridade', "Prioridade")
    )

    Medir = models.TextField(null=True, blank=True, choices=MEDIR)

    @property
    def atual(self):
        hoje = datetime.now().date()
        data = self.Data
        # abs vai me retornar um numero positivo independente da ordem
        a = abs((hoje - data).days)
        return a <= 2

    @property
    def atual2(self):
        hoje = datetime.now().date()
        data = self.Data
        # abs vai me retornar um numero positivo independente da ordem
        a = abs((hoje - data).days)
        return a

    # Referencia de nome la na view na parte ADM django
    def __str__(self):
        return '%s %s' % (self.Ss, self.Data)


class Esgoto(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    last_edited_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+', editable=False)


    Ss = models.CharField(max_length=9)
    Data = models.DateField('data', null=True, blank=True)
    Equipe = models.CharField(max_length=255, choices=Equipe())

    BAIRRO = [ ('Ipitanga', 'Ipitanga'), ('Vilas Atlântico', 'Vilas Atlântico'), ('Caji', 'Caji'), ('Areia Branca', 'Areia Branca'), ('Portao', 'Portão'), ('Vila Praiana', 'Vila Praiana'), ('Aracui', 'Aracui'), ('Jockey Clube', 'Jockey Clube'), ('Pitangueiras', 'Pitangueiras'), ('Centro', 'Centro'), ('Buraquinho', 'Buraquinho'), ('Castanheiras', 'Castanheiras'), ('Itinga', 'Itinga'), ('São Cristóvão', 'São Cristóvão'), ('Cassange', 'Cassange'), ('"Est do Coco', 'Est do Coco'), ('Jd Aeroporto', 'Jd Aeroporto'), ('Pa do Flamengo', 'Pa do Flamengo'), ('Jambeiro', 'Jambeiro'), ('Capelao SSA', 'Capelão SSA'), ('Lot Miragem', 'Lot Miragem'), ('Jd Margaridas', 'Jd Margaridas'), ('Itinga SSA', 'Itinga SSA'), ('Ipitanga SSA', 'Ipitanga SSA'), ('Areia Branc SSA', 'Areia Branc SSA'), ]


    Bairro = models.CharField(max_length=255, choices=BAIRRO)
    Rua = models.CharField(max_length=255)
    Referencia = models.CharField(max_length=255)

    ESGOTO = (
        ("Vedacao", "Vedacao"),
        ("Consertos", "Consertos"),
        ("Desobstrucao", "Desobstrucao")
    )

    Servico = models.TextField(max_length=255, choices=ESGOTO)
    Observacao = models.CharField(max_length=255)

    CHOICES = (
        (True, "Executado"),
        (False, "Pendente")
    )

    Executado = models.BooleanField(choices=CHOICES)

    LOCALIDADE = (
        ('Salvador', "Salvador"),
        ('Lauro', "Lauro")
    )
    Localidade = models.TextField(max_length=255, choices=LOCALIDADE)

    MEDIR = (
        ('Medir', "Medir"),
        ('Normal', "Normal"),
        ('Prioridade', "Prioridade")
    )

    Medir = models.TextField(null=True, blank=True, choices=MEDIR)

    # Campo de "Prazo e Fora do Prazo"

    @property
    def atual3(self):
        hoje = datetime.now().date()
        data = self.Data
        # abs vai me retornar um numero positivo independente da ordem
        a = abs((hoje - data).days)
        return a <= 2

    @property
    def atual4(self):
        hoje = datetime.now().date()
        data = self.Data
        # abs vai me retornar um numero positivo independente da ordem
        a = abs((hoje - data).days)
        return a

    # Referencia de nome la na view na parte ADM django
    def __str__(self):
        return '%s %s' % (self.Ss, self.Data)


class Pendencias(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    last_edited_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+', editable=False)


    Ss = models.CharField(max_length=9)
    Tipo = models.CharField(max_length=255)
    Solicitante = models.CharField(max_length=255, blank=True)
    Data = models.DateField('data', null=True, blank=True)
    Detalhes = models.CharField(max_length=255)

    CHOICES = (
        (True, "Executado"),
        (False, "Pendente")
    )
    Executado = models.BooleanField(choices=CHOICES)

    LOCALIDADE = (
        ('Salvador', "Salvador"),
        ('Lauro', "Lauro")
    )

    Localidade = models.TextField(max_length=255, choices=LOCALIDADE)

    MEDIR = (
        ('Medir', "Medir"),
        ('Normal', "Normal"),
        ('Prioridade', "Prioridade")
    )

    Medir = models.TextField(null=True, blank=True, choices=MEDIR)
    # Campo de "Prazo e Fora do Prazo"
    # Referencia de nome la na view na parte ADM django

    def __str__(self):
        return '%s %s' % (self.Tipo, self.Detalhes)


