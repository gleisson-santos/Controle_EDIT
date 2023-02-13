from django import forms
from django.forms import ModelForm
from datetime import timedelta
from .models import Esgoto, Pavimento, Pendencias, Material, Lancamento


class Pavimentoform(ModelForm):
    Data = forms.DateField(label='Data', widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', }), input_formats=('%Y-%m-%d',), )
    days = forms.IntegerField(required=False)          
    serv = forms.IntegerField(required=False)          
    bairro = forms.IntegerField(required=False)          
    execut = forms.IntegerField(required=False)          

    class Meta:
        model = Pavimento
        fields = '__all__'

class Materialform(ModelForm):

    Data = forms.DateField(label='Data', widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', }), input_formats=('%Y-%m-%d',), )
    days = forms.IntegerField(required=False)          
       

    class Meta:
        model = Material
        fields = '__all__'


class Lancamentoform(ModelForm):

    Data = forms.DateField(label='Data', widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', }), input_formats=('%Y-%m-%d',), )
    days = forms.IntegerField(required=False)          
       

    class Meta:
        model = Lancamento
        fields = '__all__'

class Esgotoform(ModelForm):
    Data = forms.DateField(label='Data', widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', }), input_formats=('%Y-%m-%d',), )
    days = forms.IntegerField(required=False)  
    serv = forms.IntegerField(required=False)
    execut = forms.IntegerField(required=False)    
                                                                

    class Meta:
        model = Esgoto
        fields = '__all__'


class Pendenciasform(ModelForm):
    Data = forms.DateField(label='Data', widget=forms.DateInput(format='%Y-%m-%d',   attrs={'type': 'date', }), input_formats=('%Y-%m-%d',), )
    days = forms.IntegerField(required=False)  
    execut = forms.IntegerField(required=False)  

    class Meta:
        model = Pendencias
        fields = '__all__'

