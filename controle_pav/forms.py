from django import forms
from django.forms import ModelForm

from .models import Esgoto, Pavimento, Pendencias


class Pavimentoform(ModelForm):
    Data = forms.DateField(label='Data', widget=forms.DateInput(format='%Y-%m-%d',
                                                                attrs={'type': 'date', }), input_formats=('%Y-%m-%d',), )

    class Meta:
        model = Pavimento
        fields = '__all__'


class Esgotoform(ModelForm):
    Data = forms.DateField(label='Data', widget=forms.DateInput(format='%Y-%m-%d',
                                                                attrs={'type': 'date', }), input_formats=('%Y-%m-%d',), )

    class Meta:
        model = Esgoto
        fields = '__all__'


class Pendenciasform(ModelForm):
    Data = forms.DateField(label='Data', widget=forms.DateInput(format='%Y-%m-%d',
                                                                attrs={'type': 'date', }), input_formats=('%Y-%m-%d',), )

    class Meta:
        model = Pendencias
        fields = '__all__'
