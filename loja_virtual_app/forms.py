from django import forms
from .models import Produto

# Formulário para cadastrar o produto
class ProdutoForm(forms.ModelForm): # A classe forms.ModelForm é uma subclasse do Django Forms que cria um formulário automaticamente baseado em um modelo
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'quantidade', 'imagem']
        widgets = { # Personaliza a aparência e o comportamento de cada campo no formulário
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}), # Define a altura inicial do campo em 5 linhas
            'preco': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
            'imagem': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

