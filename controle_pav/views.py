from ast import Return
from multiprocessing import context
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator
from django.shortcuts import redirect, render

from .filters import EsgotoFilter, PavimentoFilter, PendenciasFilter, MaterialFilter, LancamentoFilter, CompraFilter
from .forms import Esgotoform, Pavimentoform, Pendenciasform, Materialform, Lancamentoform, CompraForm, ProdutoForm
from .models import Esgoto, Pavimento, Pendencias, Material, Lancamento, Compra, Produto
from django.contrib.sessions.models import Session


from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum, Max
from django.db.models import Q
import datetime

#Dados de teste de Rast API
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import JsonResponse


@login_required(redirect_field_name='redirect_to')
def orcamento(request, id=None, *args, **kwargs):
	contexto = {}
	contexto['orcamento'] = Compra.objects.get(id=id)

	return render(request, "dados/Orcamento/orcamento.html", contexto)



def lista(request):
    print(request.POST)
    template_name = 'dados/Orcamento/lista.html'
    if request.method == 'POST':
        compra_form = CompraForm(request.POST)
        produto_form = ProdutoForm(request.POST)

        if compra_form.is_valid() and produto_form.is_valid():
            compra = compra_form.save()
            produto = produto_form.save(commit=False)
            produto.compra = compra
            produto.save()
            # Resto do seu código
        return redirect('lista')

    else:
        compra_form = CompraForm()
        produto_form = ProdutoForm()
    
    compras = Compra.objects.all()
    produto = Produto.objects.all()
        

    context = {
        'compra_form': compra_form,
        'produto_form': produto_form,
        'compras': compras,
        'produto': produto,
        
    }

    return render(request, template_name, context)



# from rest_framework import generics
# from .serializers import PavimentoSerializer
# from rest_framework import serializers


# from rest_framework import generics
# from .serializers import PavimentoSerializer
# from rest_framework import serializers


# #dados API
# class Pavimentolist(generics.ListCreateAPIView):
#     queryset = Pavimento.objects.all()
#     serializer_class = PavimentoSerializer


# #Chamadas para encarts
# def encart(localidade, b):
#     qtdlf2 = b.objects.filter(Localidade=localidade, Executado='0').count()
#     cont_pav_lf2 = b.objects.filter(Localidade=localidade).count()
#     return qtdlf2, cont_pav_lf2


#Filtra de periodos
def filter_pavimento(request, tipo, filters, localidade=None, servico=None):
    current_url = request.path

    days_key = f"{current_url}_selected_days"
    serv_key = f"{current_url}_selected_serv"
    bairro_key = f"{current_url}_selected_bairro"
    execut_key = f"{current_url}_selected_execut"
    material_key = f"{current_url}_selected_mateclsrial"
    
    days = request.GET.get('days')
    serv = request.GET.get('serv')
    bairro = request.GET.get('bairro')
    execut = request.GET.get('execut')
    material = request.GET.get('material')

    if days == 'all':
        days = None
        if days_key in request.session:
            del request.session[days_key]
    elif days:
        request.session[days_key] = days
        days = int(days)
    elif days_key in request.session:
        days = int(request.session[days_key])
    else:
        days = 0
    
    if serv == 'all':
        serv = None
        if serv_key in request.session:
            del request.session[serv_key]
    elif serv:
        request.session[serv_key] = serv
    elif serv_key in request.session:
        serv = request.session[serv_key]
    
    if material == 'all':
        material = None
        if material_key in request.session:
            del request.session[material_key]
    elif material:
        request.session[material_key] = material
    elif material_key in request.session:
        material = request.session[material_key]
        
    if bairro == 'all':
        bairro = None
        if bairro_key in request.session:
            del request.session[bairro_key]
    elif bairro:
        request.session[bairro_key] = bairro
    elif bairro_key in request.session:
        bairro = request.session[bairro_key]
    
    if execut == 'all':
        execut = None
        if execut_key in request.session:
            del request.session[execut_key]
    elif execut:
        request.session[execut_key] = execut
    elif execut_key in request.session:
        execut = request.session[execut_key]

    if localidade:
        pavimentos = tipo.objects.select_related().filter(Data__gte=datetime.datetime.now() - datetime.timedelta(days=days)).filter(Localidade=localidade )
    else:
        pavimentos = tipo.objects.select_related().filter(Data__gte=datetime.datetime.now() - datetime.timedelta(days=days))
        

    if serv:
        pavimentos = pavimentos.filter(Servico=serv)
    if bairro:
        pavimentos = pavimentos.filter(BairroGestor=bairro)
    if execut:
        pavimentos = pavimentos.filter(Executado=execut)
    if material:
        pavimentos = pavimentos.filter(Item=material)


    filters = filters(request.GET, queryset=pavimentos)
    return filters


# def estoque_por_localidade(localidade=None):
#     if localidade:
#         #itens = Material.objects.filter(Localidade=localidade).values('Equipe','Localidade', 'Item').annotate(total=Sum('Qtd'), total_devolucao=Sum('Devolucao'))
#         itens = Material.objects.filter(Localidade=localidade).values('Insumados', 'Equipe','Localidade', 'Item').annotate(total=Sum('Qtd'), total_devolucao=Sum('Devolucao'), total_insumados=Sum('Insumados'))

#         for item in itens:
#             item['total'] = item['total'] - item['total_devolucao']
#             item['total_insumados'] = item['total_insumados']

#         itens1 = Lancamento.objects.filter(Localidade=localidade).values('Equipe', 'Localidade','Item').annotate(total=Sum('Qtd'))
#         for item in itens1:
#             item['total'] = item['total']

#         ult_data = Lancamento.objects.filter(Localidade=localidade).values( 'Item').annotate(ultima_data=Max('Data'))

#         for item in itens:
#             for item1 in itens1:
#                 if item['Item'] == item1['Item']:
#                     sub = item1['total'] - item['total']
#                     item['sub'] = sub

#     else:
#         itens = Material.objects.values('Insumados', 'Equipe', 'Localidade', 'Item').annotate(total=Sum('Qtd'), total_devolucao=Sum('Devolucao'))

#         for item in itens:
#             item['total'] = item['total'] - item['total_devolucao']

#         itens1 = Lancamento.objects.values('Equipe','Localidade','Item').annotate(total=Sum('Qtd'))

#         ult_data = Lancamento.objects.values( 'Item').annotate(ultima_data=Max('Data'))

#         for item in itens:
#             for item1 in itens1:
#                 if item['Item'] == item1['Item']:
#                     sub = item1['total'] - item['total']
#                     item['sub'] = sub

#   return itens, ult_data, itens1


def estoque_por_localidade(localidade=None):
    filtros = Q()
    if localidade:
        filtros &= Q(Localidade=localidade)
        # em values informamos as colunas que devem ser agrupadas ou mostradas na tabela - nn
    itens = Material.objects.filter(filtros).values('Localidade', 'Item').annotate(total=Sum('Qtd') - Sum('Devolucao'), total_insumados=Sum('Insumados'), resumo_insumos=Sum('Qtd') - Sum('Insumados') - Sum('Devolucao'))
    
    teste10 = Material.objects.filter(filtros).values('EquipeGestor','Localidade', 'Item').annotate(total=Sum('Qtd') - Sum('Devolucao'), total_insumados=Sum('Insumados'), resumo_insumos=Sum('Qtd') - Sum('Insumados') - Sum('Devolucao'))

    itens1 = Lancamento.objects.filter(filtros).values('EquipeGestor', 'Localidade', 'Item').annotate(total=Sum('Qtd'))

    ult_data = Lancamento.objects.filter(filtros).values('Item').annotate(ultima_data=Max('Data'))

    for item in itens:
        for item1 in itens1:
            if item['Item'] == item1['Item']:
                sub = item1['total'] - item['total']
                item['sub'] = sub

    return itens, ult_data, itens1, teste10


# PÁGINA PRINCIPAL Material
@login_required
def index2(request):
    template_name = ('dados/index2.html')

    if request.method == 'POST':
        lancamento_form = Lancamentoform(request.POST)
        saida_form = Materialform(request.POST)

        if request.POST.get('entrada') == 'Entrada1':
            if lancamento_form.is_valid():
                instance = lancamento_form.save(commit=False)
                instance.created_by = request.user
                instance.save()
                return redirect('index2')
        elif request.POST.get('saida') == 'Saida1':
            if saida_form.is_valid():
                instance = saida_form.save(commit=False)
                instance.created_by = request.user
                instance.save()
                return redirect('index2')
    else:
        lancamento_form = Lancamentoform()
        saida_form = Materialform()
 

    geral, geral_data, geral1,uuu = estoque_por_localidade(localidade="")
    gerallf, geral_datalf, geral1lf,eee = estoque_por_localidade(localidade="Lauro")
    geralssa, geral_datassa, geral1ssa,kkk= estoque_por_localidade(localidade="Salvador")

    context = {
        'geral': geral,
        'geral_data': geral_data,
        'geral1': geral1,
        'uuu': uuu,

        'gerallf': gerallf,
        'geral_datalf': geral_datalf,
        'eee': eee,

        'geralssa': geralssa,
        'geral_datassa': geral_datassa,
        'geral1ssa': geral1ssa,
        'kkk': kkk,

        'saida_form': saida_form,
        'lancamento_form': lancamento_form,

    }

    return render(request, template_name, context)


# PÁGINA PRINCIPAL
@login_required
def index(request):
    template_name = ('dados/index.html')

    if request.method == 'POST':
        pendencia_form = Pendenciasform(request.POST)
        esgoto1_form = Esgotoform(request.POST)
        pavimento2_form = Pavimentoform(request.POST)

        if request.POST.get('gravar') == 'Pendencia':
            if pendencia_form.is_valid():
                instance = pendencia_form.save(commit=False)
                instance.created_by = request.user
                instance.save()
                pendencia_form = Pendenciasform()
        elif request.POST.get('gravar') == 'Esgoto1':
            if esgoto1_form.is_valid():
                instance = esgoto1_form.save(commit=False)
                instance.created_by = request.user
                instance.save()
                esgoto1_form = Esgotoform()
        elif request.POST.get('gravar') == 'Pav1':
            if pavimento2_form.is_valid():
                instance = pavimento2_form.save(commit=False)
                instance.created_by = request.user
                instance.save()
                pavimento2_form = Pavimentoform()
    else:
        pendencia_form = Pendenciasform()
        esgoto1_form = Esgotoform()
        pavimento2_form = Pavimentoform()
  

    def count_loc(localidade):
        pav_loc = Esgoto.objects.filter(Localidade=localidade, Executado='0').count()
        esg_loc = Pavimento.objects.filter(Localidade=localidade, Executado='0').count()
        pend_loc = Pendencias.objects.filter(Localidade=localidade, Executado='0').count()
        return pav_loc, esg_loc, pend_loc

    def count_pavimentos(localidade, servico):
        pavimento = Pavimento.objects.filter(Localidade=localidade, Servico=servico, Executado='0').count()
        esgoto = Esgoto.objects.filter(Localidade=localidade, Servico=servico, Executado='0').count()
        return pavimento, esgoto

    #Card Pavimento
    pav_pendlf = count_loc("Lauro")[1]
    Asfaltolf = count_pavimentos("Lauro", "Asfalto")[0]
    Concretolf = count_pavimentos("Lauro", "Concreto")[0]
    
    pav_pendssa = count_loc("Salvador")[1]
    Asfaltossa = count_pavimentos("Salvador", "Asfalto")[0]
    Concretossa = count_pavimentos("Salvador", "Concreto")[0]

    pav_pend = Pavimento.objects.filter(Executado='0').count()
    Asfalto = Pavimento.objects.filter(Servico='Asfalto', Executado='0').count()
    Concreto = Pavimento.objects.filter(Servico='Concreto', Executado='0').count()

    #Card Esgoto
    esg_pendlf = count_loc("Lauro")[0]
    Vedaçãolf = count_pavimentos("Lauro", "Vedacao")[1]
    Consertoslf = count_pavimentos("Lauro", "Consertos")[1]
    Desobstruçãolf = count_pavimentos("Lauro", "Desobstrucao")[1]

    esg_pendssa = count_loc("Salvador")[0]
    Vedaçãossa = count_pavimentos("Salvador", "Vedacao")[1]
    Consertosssa = count_pavimentos("Salvador", "Consertos")[1]
    Desobstruçãossa = count_pavimentos("Salvador", "Desobstrucao")[1]

    esg_pend = Esgoto.objects.filter(Executado='0').count()
    Vedação = Esgoto.objects.filter(Servico='Vedacao', Executado='0').count()
    Consertos = Esgoto.objects.filter(   Servico='Consertos', Executado='0').count()
    Desobstrução = Esgoto.objects.filter(   Servico='Desobstrucao', Executado='0').count()

    #Card Pendencia
    Pendencialf = count_loc("Lauro")[2]
    Pendenciassa = count_loc("Salvador")[2]    
    Pendencia = Pendencias.objects.filter(Executado='0').count()

    Pendencialf = Pendencias.objects.filter(  Localidade="Lauro", Executado='0').count()
    Pendenciassa = Pendencias.objects.filter(  Localidade="Salvador", Executado='0').count()

    #Filtro das tabelas
    lauro = Pendencias.objects.order_by("Executado", "Data").filter(Localidade='Lauro', Executado='0').all()
    filterlauro = PendenciasFilter(request.GET, queryset=lauro)

    salvador = Pendencias.objects.order_by("Executado", "Data").filter(Localidade='Salvador', Executado='0').all()
    filtersalvador = PendenciasFilter(request.GET, queryset=salvador)
    
    dados2 = Pendencias.objects.order_by("Executado", "Data").filter(Executado='0').all()
    dados = PendenciasFilter(request.GET, queryset=dados2)

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
        pavimento22_form = Pavimentoform(request.POST)
        if pavimento22_form.is_valid():
            instance = pavimento22_form.save(commit=False)
            instance.created_by = request.user
            instance.save()
        return redirect('pavimentos')
    else:
        pavimento22_form = Pavimentoform()

    #Filtros para tabela de Pavimento
    localidades = ['', 'Lauro', 'Salvador']
    dados, filterlauro, filtersalvador = [filter_pavimento(request, Pavimento, PavimentoFilter, localidade=l) for l in localidades]

    context = {
        'filtro': dados,
        'pavimento9': pavimento22_form,
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
        esgoto1_form = Esgotoform()


    #Filtros para tabela de Pavimento
    dados2 = filter_pavimento(request,  Esgoto, EsgotoFilter, localidade='')
    filterlauro  = filter_pavimento(request,  Esgoto, EsgotoFilter, localidade='Lauro')
    filtersalvador  = filter_pavimento(request, Esgoto, EsgotoFilter, localidade='Salvador')

    context = {
        'dados': dados2,
        'filtro2': dados2,

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
        pavimento_form = Esgotoform()
        formulario = {'formulario': pavimento_form  }

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


# Pendencias
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
        pendencia_form = Pendenciasform()


    #Filtros para tabela de Pavimento
    dados = filter_pavimento(request, Pendencias, PendenciasFilter, localidade='')
    filterlauro  = filter_pavimento(request,  Pendencias, PendenciasFilter, localidade='Lauro')
    filtersalvador  = filter_pavimento(request, Pendencias, PendenciasFilter, localidade='Salvador')


    context = {
        'filtro3': dados,
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
        pendencia_form = Pendenciasform()
        formulario = {
            'formulario': pendencia_form
        }
        return render(request, 'dados/Pendencias/criarinfo.html', context=formulario)


@ login_required
def excluir_p(request, id_pendencia):
    pendencia = Pendencias.objects.get(pk=id_pendencia)
    if request.method == 'POST':
        pendencia.delete()
        return redirect('index')
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



#Material
@ login_required
def listagem(request):
    template_name = 'dados/Material/listagem.html'

    geral, geral_data, geral1, aaa = estoque_por_localidade(localidade="")    
    gerallf, geral_datalf, geral1lf, bbb = estoque_por_localidade(localidade="Lauro")
    geralssa, geral_datassa, geral1ssa, ccc = estoque_por_localidade(localidade="Salvador")

    context = {

        'geral': geral,
        'geral_data': geral_data,
        'geral1': geral1,
        'aaa': aaa,

        'gerallf': gerallf,
        'geral_datalf': geral_datalf,
        'geral1lf': geral1lf,
        'bbb': bbb,

        'geralssa': geralssa,
        'geral_datassa': geral_datassa,
        'geral1ssa': geral1ssa,
        'ccc': ccc,
   
    }

    return render(request, template_name, context)


@ login_required
def geral_eqps(request):
    template_name = 'dados/Material/geral_eqps.html'

    geral, geral_data, geral1, aaa = estoque_por_localidade(localidade="")
    gerallf, geral_datalf, geral1lf, bbb = estoque_por_localidade(localidade="Lauro")
    geralssa, geral_datassa, geral1ssa,ccc = estoque_por_localidade(localidade="Salvador")


    context = {

        'geral': geral,
        'geral_data': geral_data,
        'geral1': geral1,
        'aaa': aaa,

        'gerallf': gerallf,
        'geral_datalf': geral_datalf,
        'geral1lf': geral1lf,
        'bbb': bbb,

        'geralssa': geralssa,
        'geral_datassa': geral_datassa,
        'geral1ssa': geral1ssa,
        'ccc': ccc,

   
    }

    return render(request, template_name, context)


@ login_required
def material(request):
    template_name = 'dados/Material/material.html'

    # Cadastro Pavimento
    if request.method == 'POST':
        material_form = Materialform(request.POST)
        if material_form.is_valid():
            print(material_form.cleaned_data)
            instance = material_form.save(commit=False)
            instance.created_by = request.user
            instance.save()
        return redirect('material')
    else:
        material_form = Materialform()

    #Filtros para tabela de Pavimento
    dados = filter_pavimento(request, Material, MaterialFilter, localidade='')
    filterlauro  = filter_pavimento(request,  Material, MaterialFilter, localidade='Lauro')
    filtersalvador  = filter_pavimento(request, Material, MaterialFilter, localidade='Salvador')


    context = {
        'dados': dados2,
        'filtro': dados,
        'days': days,

        #Cart Pavimento
        # 'cont_pav_lf':cont_pav_lf,
        # 'cont_pav_ssa':cont_pav_ssa,
        'cont_pav':cont_pav,

        'pavimento9': material_form,
        'localidade_l': filterlauro,
        'localidade_2': filtersalvador,
   
    }

    return render(request, template_name, context)



@ login_required
def inserir_material(request):
    if request.method == 'POST':
        material_form = Materialform(request.POST)
        if material_form.is_valid():
            instance = material_form.save(commit=False)
            instance.created_by = request.user
            instance.save()
        return redirect('novo_pavimento')
    else:
        material_form = Materialform()
        formulario = {'formulario': material_form}
        return render(request, 'dados/Material/inserir_material.html', context=formulario)


@ login_required
def editar_m(request, id_material):
    material = Material.objects.get(pk=id_material)
    criador = material.created_by
    if request.method == 'GET':
        # instance vai deixar o dormulario com os itens ja preenchidos de forma visiveis 'populado'
        formulario = Materialform(instance=material)
        return render(request, 'dados/Material/inserir_material.html', {'formulario': formulario})
    else:
        formulario = Materialform(request.POST, instance=material)
        if formulario.is_valid():
            item = formulario.save(commit=False)
            item.created_by = criador
            item.last_edited_by = request.user
            item.save()
        return redirect('material')


@ login_required
def editar_entrada(request, id_lancamento):
    material = Lancamento.objects.get(pk=id_lancamento)
    criador = material.created_by
    if request.method == 'GET':
        # instance vai deixar o dormulario com os itens ja preenchidos de forma visiveis 'populado'
        formulario = Lancamentoform(instance=material)
        return render(request, 'dados/Material/editar_entrada.html', {'formulario': formulario})
    else:
        formulario = Lancamentoform(request.POST, instance=material)
        if formulario.is_valid():
            item = formulario.save(commit=False)
            item.created_by = criador
            item.last_edited_by = request.user
            item.save()
        return redirect('lancamentos')


@ login_required
def excluir_m(request, id_material):
    material = Material.objects.get(pk=id_material)
    if request.method == 'POST':
        material.delete()
        return redirect('material')
    return render(request, 'dados/Material/exluir_material.html', {'item': material})


@ login_required
def lancamentos(request):
    template_name = 'dados/Material/lancamentos.html'

    # Cadastro Pavimento
    if request.method == 'POST':
        lancamento_form = Lancamentoform(request.POST)
        if lancamento_form.is_valid():
            instance = lancamento_form.save(commit=False)
            instance.created_by = request.user
            instance.save()
        return redirect('lancamentos')
    else:
        print("cuuuuuuuuuuuuuuuuuu")
        lancamento_form = Lancamentoform()

    #Filtros para tabela de Pavimento
    dados = filter_pavimento(request, Lancamento, LancamentoFilter, localidade='')

    filterlauro  = filter_pavimento(request,  Lancamento, LancamentoFilter, localidade='Lauro')
    filtersalvador  = filter_pavimento(request, Lancamento, LancamentoFilter, localidade='Salvador')
   
    context = {
        'filtro': dados,
        'localidade_l': filterlauro,
        'localidade_2': filtersalvador,
        'pavimento9': lancamento_form,
    }

    return render(request, template_name, context)

