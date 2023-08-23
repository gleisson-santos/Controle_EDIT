
import django_filters
from .models import Esgoto, Pavimento, Pendencias, Material, Lancamento
from datetime import timedelta




class PavimentoFilter(django_filters.FilterSet):

    # Bairro = django_filters.CharFilter(lookup_expr='iexact')
    Servico = django_filters.CharFilter(lookup_expr='iexact')
    Ss_Final = django_filters.CharFilter(lookup_expr='icontains')
    Ss = django_filters.CharFilter(lookup_expr='contains')
    Executado = django_filters.CharFilter(lookup_expr='exact')
    
    # Constante
    Executado = ('A', 'B')
    Servico = ('Asfalto', 'Concreto', 'Blocos')

    class Meta:
        model = Pavimento
        fields = ('Servico', 'Executado')


class EsgotoFilter(django_filters.FilterSet):
    Ss = django_filters.CharFilter(lookup_expr='iexact')
    Data = django_filters.DateFilter(lookup_expr='exact')
    Bairro = django_filters.CharFilter(lookup_expr='iexact')
    Executado = django_filters.CharFilter(lookup_expr='exact')
    Servico = django_filters.CharFilter(lookup_expr='iexact')

    # constante
    Executado = ('A', 'B')
    Servico = ('Vedacao', 'Consertos', 'Desobstrucao')

    class Meta:
        model = Esgoto
        fields = ('Servico', 'Data', 'Bairro', 'Executado')


class PendenciasFilter(django_filters.FilterSet):
    Executado = django_filters.CharFilter(lookup_expr='exact')
    Data = django_filters.DateFilter(lookup_expr='exact')

    # constante
    Executado = ('A', 'B')

    class Meta:
        model = Pendencias
        fields = ('Executado', 'Data')


class MaterialFilter(django_filters.FilterSet):

    # constante
    class Meta:
        model = Material
        fields = '__all__'


class LancamentoFilter(django_filters.FilterSet):

    # constante
    class Meta:
        model = Lancamento
        fields = '__all__'

