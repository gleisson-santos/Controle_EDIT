from datetime import date, datetime
from random import choices

from django.db import models

# modelos que irão representar uma tabela no banco de dados


class Pavimento(models.Model):
    Ss = models.TextField(max_length=255)
    Data = models.DateField('data', null=True, blank=True)
    Prazo = models.BooleanField(default=False)

    EQUIPE = (
        ("Eq213-Silvio",   "Eq213-Silvio"),
        ("Eq221-Edcarlos",   "Eq221-Edcarlos"),
        ("Eq214-Cristiano",   "Eq214-Cristiano"),
        ("Eq218A-Jilton",  "Eq218A-Jilton"),
        ("Eq309A-Roberio", "Eq309A-Roberio"),
        ("Eq224A-Haroldo", "Eq224A-Haroldo"),
        ("Eq215A-Narciso", "Eq215A-Narciso"),
        ("Eq320A-Celio",   "Eq320A-Celio"),
        ("Eq315A-Hanilton", "Eq315A-Hanilton"),
        ("Eq218A-Jilton", "Eq218A-Jilton"),
        ("Eq308A-Adailton", "Eq308A-Adailton"),

        ("EqEsgoto-Esgoto", "EqEsgoto-Esgoto"),
        ("EqMoto-Motoqueiro", "EqMoto-Motoqueiro"),

    )

    Equipe = models.TextField(max_length=255, choices=EQUIPE)
    Bairro = models.TextField(max_length=255)
    Rua = models.TextField(max_length=255)
    Referencia = models.TextField(max_length=255)

    SERVICO = (
        ("Asfalto", "Asfalto"),
        ("Concreto", "Concreto"),
        ("Blocos", "Blocos")
    )

    Servico = models.TextField(max_length=255, choices=SERVICO)

    Metragem = models.TextField(max_length=255)
    Observacao = models.TextField(max_length=255, blank=True)
    Ss_Final = models.TextField(max_length=255, blank=True)
    Met_Final = models.TextField(max_length=255, blank=True)

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
    Ss = models.TextField(max_length=255)
    Data = models.DateField('data', null=True, blank=True)

    EQUIPE = (
        ("Eq307E-Ailton", "Eq307E-Ailton"),
        ("Eq222E-Gilvando", "Eq222E-Gilvando"),
        ("Eq227E-Carlos", "Eq227E-Carlos"),

        ("EqEsgoto-Esgoto", "EqEsgoto-Esgoto"),
        ("EqMoto-Motoqueiro", "EqMoto-Motoqueiro"),
        ("EqAgua-Vazamento", "EqAgua-Vazamento")
    )

    Equipe = models.TextField(max_length=255, choices=EQUIPE)
    Bairro = models.TextField(max_length=255)
    Rua = models.TextField(max_length=255)
    Referencia = models.TextField(max_length=255)

    ESGOTO = (
        ("Vedacao", "Vedacao"),
        ("Consertos", "Consertos"),
        ("Desobstrucao", "Desobstrucao")
    )

    Servico = models.TextField(max_length=255, choices=ESGOTO)
    Observacao = models.TextField(max_length=255, blank=True)

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
    Ss = models.TextField(max_length=255)
    Tipo = models.TextField(max_length=255)
    Solicitante = models.TextField(max_length=255, blank=True)
    Data = models.DateField('data', null=True, blank=True)
    Detalhes = models.TextField(max_length=255)

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
