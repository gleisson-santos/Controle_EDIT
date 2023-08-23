from unicodedata import name
from django.contrib import admin
from django.urls import include, path
from accounts import views
from controle_pav import views
# from controle_pav.views import Pavimentolist


urlpatterns = [
    # path de pavimento agua
    path('admin/',         admin.site.urls),
    path('',  views.index,         name='index'),
    

    path('Pavimentos/pavimentos',                                views.pavimentos,    name='pavimentos'),
    path('Pavimentos/novo_pavimento/',                           views.criar,         name='novo_pavimento'),
    path('Pavimentos/novo_pavimento/<int:id_pavimento>',         views.editar,        name='editar'),

    path('Pavimentos/pavimentos',                                views.pavimentos,    name='pavimentos'),
    path('Pavimentos/novo_pavimento/',                           views.criar,         name='novo_pavimento'),

    path('Pavimentos/novo_pavimento/<int:id_pavimento>',         views.editar,        name='editar'),

    # path('<int:pk>/',         views.expense_detail,        name='expense_detail'),
    # path('<int:pk>/update/',         views.expense_update,       name='expense_update'),


     path('Pavimentos/excluir_pavimento/<int:id_pavimento>',                 views.excluir,       name='excluir'),
     path('<int:id_pavimento>',                                              views.detalhe,       name='detalhe'),
     path('accounts/',                                                       include('accounts.urls')),   
     path('accounts/',                                                       include('django.contrib.auth.urls')),

    # path de esgoto
     path('Esgoto/pavimentos2',                                              views.pavimentos2,    name='pavimentos2'),
     path('Esgoto/novo_esgoto/',                                             views.criar2,         name='novo_esgoto'),
     path('Esgoto/novo_esgoto/<int:id_pavimento2>',                          views.editar2,        name='editar2'),
     path('Esgoto/excluir_pavimento2/<int:id_pavimento2>',                   views.excluir2,       name='excluir2'),
     path('Esgoto/<int:id_pavimento2>',                                      views.detalhe2,       name='detalhe2'),

    # path de pendencias
    path('Pendencias/informativo/',                                              views.informativo, name='informativo'),
    path('Pendencias/criarinfo/',                                                views.criarinfo,   name='criarinfo'),
    path('Pendencias/criarinfo/<int:id_pendencia>',                              views.editar_p,        name='editar_p'),
    path('Pendencias/excluir_pendencia/<int:id_pendencia>',                      views.excluir_p,       name='excluir_p'),


    # path de Material
    path('Material/material/',                                                          views.material, name='material'),
    path('Material/inserir_material/',                                                   views.inserir_material,   name='inserir_material'),
    path('Material/inserir_material/<int:id_material>',                                  views.editar_m,        name='editar_m'),

    path('Material/editar_entrada/<int:id_lancamento>',                                 views.editar_entrada,        name='editar_entrada'),
    
    path('Material/exluir_material/<int:id_material>',                                  views.excluir_m,       name='excluir_m'),
    path('index2/',                                 views.index2,           name='index2'),
    path('Material/listagem/',                      views.listagem,         name='listagem'),

    path('Material/lancamentos/',                   views.lancamentos,      name='lancamentos'),
    path('Material/geral_eqps/',                    views.geral_eqps,       name='geral_eqps'),


    # path de Orçamento
    path('orcamento/<int:id>/',                                  views.orcamento, name='orcamento'),
    path('lista/',                                               views.lista,     name='lista'),

    # path('pessoas/', Pavimentolist.as_view(), name='pessoa-list'),

]


# from django.conf import settings

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns = [
#         path('__debug__/', include(debug_toolbar.urls)),
#     ] + urlpatterns