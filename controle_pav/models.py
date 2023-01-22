from csv import reader
from datetime import date, datetime
from random import choices
from django.db import models
import pandas as pd


# df = pd.read_csv("C:/Users/55719/Desktop/#Projeto - Controle_servcio_EDIT/Controle_EDIT/controle_pav/static/texto/equipes.csv", header=None)
# # print(df.head())

def Equipe():
    with open("controle_pav/static/texto/equipes.csv", 'r') as arquivo:
        equipes = arquivo.read()
        EQUIPE = (
                ('equipes', equipes.split()[0]),
                ('equipes', equipes.split()[1]),
                ('equipes', equipes.split()[2]),
                ('equipes', equipes.split()[3]),
                ('equipes', equipes.split()[4]),
                ('equipes', equipes.split()[5]),
            )
        return EQUIPE



# modelos que irão representar uma tabela no banco de dados
class Pavimento(models.Model):
    Ss = models.CharField(max_length=9)
    Data = models.DateField('data', null=True, blank=True)
    Prazo = models.BooleanField(default=False)

    Equipe = models.CharField(max_length=255, choices=Equipe())
    Bairro = models.CharField(max_length=255)
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

    Executado = models.BooleanField(default=False, choices=EXECUTADO)

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
    Ss = models.CharField(max_length=9)
    Data = models.DateField('data', null=True, blank=True)

    Equipe = models.CharField(max_length=255, choices=Equipe())
    Bairro = models.CharField(max_length=255)
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
