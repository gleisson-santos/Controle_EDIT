import csv
from datetime import date, datetime
from random import choices
from django.db import models
import pandas as pd
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.utils import timezone


def Equipe700():
    with open("controle_pav/static/texto/Equipes-700.csv", 'r') as arquivo:
        equipes = arquivo.read().splitlines()
        EQUIPE700 = [(equipe, equipe) for equipe in equipes]
    return EQUIPE700

def Equipe900():
    with open("controle_pav/static/texto/Equipes-900.csv", 'r') as arquivo:
        equipes = arquivo.read().splitlines()
        EQUIPE900 = [(equipe, equipe) for equipe in equipes]
    return EQUIPE900

def EquipeGestor():
    with open("controle_pav/static/texto/EquipesGestor.csv", 'r') as arquivo:
        equipes = arquivo.read().splitlines()
        EQUIPEGESTOR = [(equipe, equipe) for equipe in equipes]
    return EQUIPEGESTOR


#Bairros
def Bairro700():
    with open("controle_pav/static/texto/Bairros-700.csv", 'r') as arquivo:
        bairros = arquivo.read().splitlines()
        BAIRRO700 = [(bairro, bairro) for bairro in bairros]
    return BAIRRO700

def Bairro900():
    with open("controle_pav/static/texto/Bairros-900.csv", 'r') as arquivo:
        bairros = arquivo.read().splitlines()
        BAIRRO900 = [(bairro, bairro) for bairro in bairros]
    return BAIRRO900

def BairroGestor():
    with open("controle_pav/static/texto/BairrosGestor.csv", 'r') as arquivo:
        bairros = arquivo.read().splitlines()
        BAIRROGESTOR = [(bairro, bairro) for bairro in bairros]
    return BAIRROGESTOR


def Material():
    with open("controle_pav/static/texto/Materiais.csv", 'r', encoding='utf-8') as arquivo:
        materiais = arquivo.read().splitlines()
        MATERIAL = [(material, material) for material in materiais]
    return MATERIAL

   


# modelos que irão representar uma tabela no banco de dados
class Pavimento(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    last_edited_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+', editable=False)
     
    Ss = models.CharField(max_length=9)
    Data = models.DateField('data', null=True, blank=True)
    Prazo = models.BooleanField(default=False)

    Equipe700 = models.CharField(max_length=255, choices=Equipe700(), blank=True)
    Equipe900 = models.CharField(max_length=255, choices=Equipe900(), blank=True)
    EquipeGestor = models.CharField(max_length=255,choices=EquipeGestor(), blank=True)

    Bairro700 = models.CharField(max_length=255, choices=Bairro700(),  blank=True)
    Bairro900 = models.CharField(max_length=255, choices=Bairro900(),  blank=True)
    BairroGestor = models.CharField(max_length=255, choices=BairroGestor(),  blank=True)

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

class MaterialBase(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    last_edited_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+', editable=False)
     
    Equipe = models.CharField(max_length=255, choices=Bairro700(), blank=True)
    Data = models.DateField('data', null=True, blank=True)
    Item = models.CharField(max_length=800, choices=Material())
    N_reserva = models.IntegerField(blank=True, null=True)

    Qtd = models.IntegerField(blank=False)

    SERVICO = (
        ("Operacional", "Operacional"),
        ("Comercial", "Comercial"),
        ("Unid. Tec", "Unid. Tec")
    )
    Servico = models.CharField(max_length=255, choices=SERVICO, blank=True)

    EXECUTADO = (
        (True, "Executado"),
        (False, "Pendente")
    )

    Executado = models.BooleanField(default=False, choices=EXECUTADO, blank=True)


    LOCALIDADE = (
        ("Salvador", "Salvador"),
        ("Lauro", "Lauro")
    )
    Localidade = models.TextField(max_length=255, choices=LOCALIDADE)
    Observacao = models.CharField(max_length=255, blank=True)
    Devolucao = models.IntegerField(blank=True, null=True,  default=0)
    Insumados = models.IntegerField(blank=True, null=True,  default=0)


    # Referencia de nome la na view na parte ADM django
    def __str__(self):
        return '%s %s' % (self.Equipe, self.Item)

class Lancamento(MaterialBase):
    class Meta:
        # proxy = True Essa desgraça aqui atrasou o meu lado
        verbose_name = "Lancamento"
        verbose_name_plural = "Lançamentos"

class Material(MaterialBase):
    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materiais"

class Esgoto(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    last_edited_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+', editable=False)


    Ss = models.CharField(max_length=9)
    Data = models.DateField('data', null=True, blank=True)


    Equipe700 = models.CharField(max_length=255, choices=Equipe700(), blank=True)
    Equipe900 = models.CharField(max_length=255, choices=Equipe900(), blank=True)
    EquipeGestor = models.CharField(max_length=255,choices=EquipeGestor(), blank=True)

    Bairro700 = models.CharField(max_length=255, choices=Bairro700(),  blank=True)
    Bairro900 = models.CharField(max_length=255, choices=Bairro900(),  blank=True)
    BairroGestor = models.CharField(max_length=255, choices=BairroGestor(),  blank=True)


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
        data_limite = self.Data
        if self.Servico == 'Consertos':
            prazo = timezone.timedelta(days=3)
        elif self.Servico == 'Vedacao' or'Desobstrucao':
            prazo = timezone.timedelta(days=1)
        else:
            prazo = timezone.timedelta(days=2)
        dias_restantes = abs((data_limite - timezone.now().date()).days)
        if self.Servico == 'Vedacao' and dias_restantes <= 1:
            return 
        elif dias_restantes <= prazo.days:
            return 
        else:
            return f' {dias_restantes - prazo.days}'

    # @property
    # def atual4(self):
    #     hoje = datetime.now().date()
    #     data = self.Data
    #     # abs vai me retornar um numero positivo independente da ordem
    #     a = abs((hoje - data).days)
    #     return a

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


