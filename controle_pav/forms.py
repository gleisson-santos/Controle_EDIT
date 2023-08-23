from django import forms
from django.forms import ModelForm
from datetime import timedelta
from .models import Esgoto, Pavimento, Pendencias, Material, Lancamento, Compra, Produto, Fornecedor, Materiall
from django.forms import DateInput


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





#---------------------------------------------------------------------

# class CompraForm(forms.ModelForm):
#     fornecedor = forms.CharField(max_length=200, label='Fornecedor')
#     material = forms.CharField(max_length=200, label='Material')

#     class Meta:
#         model = Compra
#         fields = ['fornecedor', 'nota_fiscal', 'data']


# class ProdutoForm(forms.ModelForm):
#     material = forms.CharField(max_length=200, label='Material')

#     class Meta:
#         model = Produto
#         fields = ['material', 'preco', 'quantidade']
        

class CompraForm(forms.ModelForm):
    fornecedor = forms.ModelChoiceField(
        queryset=Fornecedor.objects.all(),
        label='Fornecedor',
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = Compra
        fields = ['fornecedor', 'nota_fiscal', 'data']
        widgets = {
            'data': DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

class ProdutoForm(forms.ModelForm):
    material = forms.ModelChoiceField(
        queryset=Materiall.objects.all(),
        label='Material',
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = Produto
        fields = ['material', 'preco', 'quantidade']


class FornecedorForm(forms.ModelForm):
    fornecedor = forms.CharField(label='Fornecedor', max_length=200)  # Campo de texto para o nome do fornecedor
    data = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    

    class Meta:
        model = Compra
        fields = ['fornecedor', 'nota_fiscal', 'data']

class MaterialForm(forms.ModelForm):
    nome = forms.ModelChoiceField(
    queryset=Materiall.objects.all(), 
    label='Material',
    widget=forms.TextInput(attrs={'placeholder': 'Informe o material'}),
    required=False
    )
    class Meta:
        model = Materiall
        fields = '__all__'

