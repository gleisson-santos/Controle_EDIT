from django import forms
from django.forms import ModelForm

from .models import Esgoto, Pavimento, Pendencias, Contact 


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


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')