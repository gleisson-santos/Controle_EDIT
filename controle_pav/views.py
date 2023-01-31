
from ast import Return
from multiprocessing import context

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import redirect, render

from .filters import EsgotoFilter, PavimentoFilter, PendenciasFilter
from .forms import Esgotoform, Pavimentoform, Pendenciasform
from .models import Esgoto, Pavimento, Pendencias


from django.contrib.auth.models import User
from django.db import models


# PÁGINA PRINCIPAL
@login_required
def index(request):
    template_name = ('dados/index.html')

    # Cadastro Pendencias
    if request.method == 'POST':
        pendencia_form = Pendenciasform(request.POST)
        if request.POST['gravar'] == 'Pendencia':
            if pendencia_form.is_valid():
                instance = pendencia_form.save(commit=False)
                instance.created_by = request.user
                instance.save()
                return redirect('index')
            else:
                print(form.errors)
    else:
        pendencia_form = Pendenciasform()

    # Cadastro Esgoto
    if request.method == 'POST':
        esgoto1_form = Esgotoform(request.POST)
        if request.POST['gravar'] == 'Esgoto1':
            if esgoto1_form.is_valid():
                instance = esgoto1_form.save(commit=False)
                instance.created_by = request.user
                instance.save()
                return redirect('index')
            else:
                print(form.errors)
    else:
        esgoto1_form = Esgotoform()

    # Cadastro Pavimento
    if request.method == 'POST':
        pavimento2_form = Pavimentoform(request.POST)
        if request.POST['gravar'] == 'Pav1':
            if pavimento2_form.is_valid():
                instance = pavimento2_form.save(commit=False)
                instance.created_by = request.user
                instance.save()
                return redirect('index')
            else:
                print(form.errors)
    else:
        pavimento2_form = Pavimentoform()


    dados2 = Pendencias.objects.order_by("Executado", "Data").filter(Executado='0').all()
    dados = PendenciasFilter(request.GET, queryset=dados2)

    pav_pend = Pavimento.objects.filter(Executado='0').count()
    pav_pendlf = Pavimento.objects.filter( Localidade="Lauro", Executado='0').count()
    pav_pendssa = Pavimento.objects.filter( Localidade="Salvador", Executado='0').count()

    esg_pend = Esgoto.objects.filter(Executado='0').count()
    esg_pendlf = Esgoto.objects.filter( Localidade="Lauro", Executado='0').count()
    esg_pendssa = Esgoto.objects.filter(Localidade="Salvador", Executado='0').count()

    Asfaltolf = Pavimento.objects.filter( Localidade="Lauro",  Servico='Asfalto', Executado='0').count()
    Concretolf = Pavimento.objects.filter( Localidade="Lauro",  Servico='Concreto', Executado='0').count()

    Asfaltossa = Pavimento.objects.filter(  Localidade="Salvador",  Servico='Asfalto', Executado='0').count()
    Concretossa = Pavimento.objects.filter(  Localidade="Salvador",  Servico='Concreto', Executado='0').count()

    Asfalto = Pavimento.objects.filter( Servico='Asfalto', Executado='0').count()
    Concreto = Pavimento.objects.filter(   Servico='Concreto', Executado='0').count()

    Vedaçãolf = Esgoto.objects.filter(   Localidade="Lauro", Servico='Vedacao', Executado='0').count()
    Consertoslf = Esgoto.objects.filter(    Localidade="Lauro", Servico='Consertos', Executado='0').count()
    Desobstruçãolf = Esgoto.objects.filter(    Localidade="Lauro", Servico='Desobstrucao', Executado='0').count()

    Vedaçãossa = Esgoto.objects.filter(    Localidade="Salvador", Servico='Vedacao', Executado='0').count()
    Consertosssa = Esgoto.objects.filter(     Localidade="Salvador", Servico='Consertos', Executado='0').count()
    Desobstruçãossa = Esgoto.objects.filter(     Localidade="Salvador", Servico='Desobstrucao', Executado='0').count()

    Vedação = Esgoto.objects.filter(Servico='Vedacao', Executado='0').count()
    Consertos = Esgoto.objects.filter(   Servico='Consertos', Executado='0').count()
    Desobstrução = Esgoto.objects.filter(   Servico='Desobstrucao', Executado='0').count()

    Pendencialf = Pendencias.objects.filter(   Localidade="Lauro", Executado='0').count()
    Pendenciassa = Pendencias.objects.filter(  Localidade="Salvador", Executado='0').count()
    Pendencia = Pendencias.objects.filter(Executado='0').count()

    lauro = Pendencias.objects.filter(Localidade='Lauro')
    filterlauro = PendenciasFilter( request.GET, queryset=lauro)

    salvador = Pendencias.objects.filter(Localidade='Salvador')
    filtersalvador = PendenciasFilter(  request.GET, queryset=salvador)

    context = {

        'dados': dados2,
        'filtro3': dados,

        'pav_pend': pav_pend,

        'filtrolf': pav_pendlf,
        'filtrossa': pav_pendssa,

        'esg_pend': esg_pend,
        'esg_pendlf': esg_pendlf,
        'esg_pendssa': esg_pendssa,

        'Asfaltossa': Asfaltossa,
        'Concretossa': Concretossa,

        'Asfaltolf': Asfaltolf,
        'Concretolf': Concretolf,

        'Asfalto': Asfalto,
        'Concreto': Concreto,

        'Vedaçãolf': Vedaçãolf,
        'Consertoslf': Consertoslf,
        'Desobstruçãolf': Desobstruçãolf,

        'Vedaçãossa': Vedaçãossa,
        'Consertosssa': Consertosssa,
        'Desobstruçãossa': Desobstruçãossa,

        'Vedação': Vedação,
        'Consertos': Consertos,
        'Desobstrução': Desobstrução,

        'Pendencia': Pendencia,
        'Pendencialf': Pendencialf,
        'Pendenciassa': Pendenciassa,

        'cadastro1': pendencia_form,

        'esgoto21': esgoto1_form,
        'pavimento5': pavimento2_form,

        'localidade_l': filterlauro,
        'localidade_2': filtersalvador,

    }
    return render(request, template_name, context)


# Pavimentos
@ login_required
def pavimentos(request):
    template_name = 'dados/Pavimentos/pavimentos.html'

    # Cadastro Pavimento
    if request.method == 'POST':
        form = Pavimentoform(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.created_by = request.user
            instance.save()
            return redirect('pavimentos')
        else:
            print(form.errors)
    else:
        form = Pavimentoform()


    dados2 = Pavimento.objects.order_by("Executado", "Data").all()
    dados = PavimentoFilter(request.GET, queryset=dados2)

    qtdlf = Esgoto.objects.filter(Localidade="Lauro", Executado='0').count()
    qtdssa = Esgoto.objects.filter(Localidade="Salvador", Executado='0').count()

    qtd = Pavimento.objects.filter(Executado='0').count()

    lauro = Pavimento.objects.filter(Localidade='Lauro')
    filterlauro = PavimentoFilter(request.GET, queryset=lauro)

    salvador = Pavimento.objects.filter(Localidade='Salvador')
    filtersalvador = PavimentoFilter(request.GET, queryset=salvador)

    context = {
        'dados': dados2,
        'filtro': dados,

        'qtdlf': qtdlf,
        'qtdssa': qtdssa,
        'qtd': qtd,


        'pavimento9': form,


        'localidade_l': filterlauro,
        'localidade_2': filtersalvador,

    }

    return render(request, template_name, context)


@ login_required
def detalhe(request, id_pavimento):
    dados = {'dados': Pavimento.objects.get(pk=id_pavimento)}
    return render(request, 'dados/Pavimentos/detalhe.html', dados)


@ login_required
def criar(request):
    if request.method == 'POST':
        pavimento_form = Pavimentoform(request.POST)
        if pavimento_form.is_valid():
            instance = pavimento_form.save(commit=False)
            instance.created_by = request.user
            instance.save()
            return redirect('novo_pavimento')
        else:
            print(form.errors)
    else:
        pavimento_form = Pavimentoform()
        formulario = {'formulario': pavimento_form}
        return render(request, 'dados/Pavimentos/novo_pavimento.html', context=formulario)

@ login_required
def editar(request, id_pavimento):
    pavimento = Pavimento.objects.get(pk=id_pavimento)
    criador = pavimento.created_by
    if request.method == 'GET':
        # instance vai deixar o dormulario com os itens ja preenchidos de forma visiveis 'populado'
        formulario = Pavimentoform(instance=pavimento)
        return render(request, 'dados/Pavimentos/novo_pavimento.html', {'formulario': formulario})
    else:
        formulario = Pavimentoform(request.POST, instance=pavimento)
        if formulario.is_valid():
            item = formulario.save(commit=False)
            item.created_by = criador
            item.last_edited_by = request.user
            item.save()
        return redirect('pavimentos')


@ login_required
def excluir(request, id_pavimento):
    pavimento = Pavimento.objects.get(pk=id_pavimento)
    if request.method == 'POST':
        pavimento.deleted_by = request.user
        pavimento.last_deleted_by = request.user 
        pavimento.save()
        pavimento.delete()
        return redirect('pavimentos')
    return render(request, 'dados/Pavimentos/confirmar_exclusao.html', {'item': pavimento})


# Esgoto
@ login_required
def pavimentos2(request):
    template_name = 'dados/Esgoto/pavimentos2.html'

    # Cadastro Esgoto
    if request.method == 'POST':
        esgoto1_form = Esgotoform(request.POST)
        if esgoto1_form.is_valid():
            instance = esgoto1_form.save(commit=False)
            instance.created_by = request.user
            instance.save()
            return redirect('pavimentos2')
        else:
            print(form.errors)
    else:
        esgoto1_form = Esgotoform()

    dados2 = Esgoto.objects.order_by("Executado", "Data").all()
    dados = EsgotoFilter(request.GET, queryset=dados2)

    qtdlf = Esgoto.objects.filter(Localidade="Lauro", Executado='0').count()
    qtdssa = Esgoto.objects.filter(
        Localidade="Salvador", Executado='0').count()
    qtd = Esgoto.objects.filter(Executado='0').count()

    lauro = Esgoto.objects.filter(Localidade='Lauro')
    filterlauro = EsgotoFilter(
        request.GET, queryset=lauro)

    salvador = Esgoto.objects.filter(Localidade='Salvador')
    filtersalvador = EsgotoFilter(
        request.GET, queryset=salvador)

    context = {
        'dados': dados2,
        'filtro2': dados,

        'qtdlf': qtdlf,
        'qtdssa': qtdssa,
        'qtd': qtd,

        'localidade_l': filterlauro,
        'localidade_2': filtersalvador,

        'esgoto01': esgoto1_form,
    }

    return render(request, template_name, context)


@ login_required
def detalhe2(request, id_pavimento2):
    dados = {'dados': Esgoto.objects.get(pk=id_pavimento2)}
    return render(request, 'dados/Esgoto/detalhe2.html', dados)


@ login_required
def criar2(request):
    if request.method == 'POST':
        pavimento_form = Esgotoform(request.POST)
        if pavimento_form.is_valid():
            instance = pavimento_form.save(commit=False)
            instance.created_by = request.user
            instance.save()
            return redirect('novo_esgoto')
        else:
            print(form.errors)
    else:
        pavimento_form = Esgotoform()
        formulario = {'formulario': pavimento_form}

        return render(request, 'dados/Esgoto/novo_esgoto.html', context=formulario)


@ login_required
def editar2(request, id_pavimento2):
    pavimento2 = Esgoto.objects.get(pk=id_pavimento2)
    criador = pavimento2.created_by
    if request.method == 'GET':
        # instance vai deixar o dormulario com os itens ja preenchidos de forma visiveis 'populado'
        formulario = Esgotoform(instance=pavimento2)
        return render(request, 'dados/Esgoto/novo_esgoto.html', {'formulario': formulario})
    else:
        formulario = Esgotoform(request.POST, instance=pavimento2)
        if formulario.is_valid():
            item = formulario.save(commit=False)
            item.created_by = criador
            item.last_edited_by = request.user
            item.save()
        return redirect('pavimentos2')


@ login_required
def excluir2(request, id_pavimento2):
    pavimento2 = Esgoto.objects.get(pk=id_pavimento2)
    if request.method == 'POST':
        pavimento2.delete()
        return redirect('pavimentos2')
    return render(request, 'dados/Esgoto/confirmar_exclusao2.html', {'item': pavimento2})




# Informativos
@ login_required
def informativo(request):
    template_name = 'dados/Pendencias/informativo.html'

    # Cadastro Pendencias
    if request.method == 'POST':
        pendencia_form = Pendenciasform(request.POST)
        if pendencia_form.is_valid():
            instance = pendencia_form.save(commit=False)
            instance.created_by = request.user
            instance.save()
            return redirect('informativo')
        else:
            print(form.errors)
    else:
        pendencia_form = Pendenciasform()

    dados2 = Pendencias.objects.order_by("Executado", "Data")
    dados = PendenciasFilter(request.GET, queryset=dados2)

    qtdlf = Pendencias.objects.filter(
        Localidade="Lauro", Executado='0').count()
    qtdssa = Pendencias.objects.filter(
        Localidade="Salvador", Executado='0').count()

    qtd = Pendencias.objects.filter(Executado='0').count()

    lauro = Pendencias.objects.filter(Localidade='Lauro')
    filterlauro = PendenciasFilter(request.GET, queryset=lauro)

    salvador = Pendencias.objects.filter(Localidade='Salvador')
    filtersalvador = PendenciasFilter(request.GET, queryset=salvador)

    context = {
        'dados': dados2,
        'filtro3': dados,

        'qtdlf': qtdlf,
        'qtdssa': qtdssa,
        'qtd': qtd,

        'localidade_l': filterlauro,
        'localidade_2': filtersalvador,


        'cadastro2': pendencia_form,
    }

    return render(request, template_name, context)


@ login_required
def criarinfo(request):
    if request.method == 'POST':
        pendencia_form = Pendenciasform(request.POST)
        if pendencia_form.is_valid():
            instance = pendencia_form.save(commit=False)
            instance.created_by = request.user
            instance.save()
            return redirect('informativo')
        else:
            print(form.errors)
    else:
        pendencia_form = Pendenciasform()
        formulario = { 'formulario': pendencia_form}
        return render(request, 'dados/Pendencias/criarinfo.html', context=formulario)


@ login_required
def excluir_p(request, id_pendencia):
    pendencia = Pendencias.objects.get(pk=id_pendencia)
    if request.method == 'POST':
        pendencia.delete()
        return redirect('informativo')
    return render(request, 'dados/Pendencias/excluir_pendencia.html', {'item': pendencia})


@ login_required
def editar_p(request, id_pendencia):
    pendencia = Pendencias.objects.get(pk=id_pendencia)
    criador = pendencia.created_by
    if request.method == 'GET':
        # instance vai deixar o dormulario com os itens ja preenchidos de forma visiveis 'populado'
        formulario = Pendenciasform(instance=pendencia)
        return render(request, 'dados/Pendencias/criarinfo.html', {'formulario': formulario})
    else:
        formulario = Pendenciasform(request.POST, instance=pendencia)
        if formulario.is_valid():
            item = formulario.save(commit=False)
            item.created_by = criador
            item.last_edited_by = request.user
            item.save()
        return redirect('informativo')
