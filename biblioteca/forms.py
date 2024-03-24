from .models import Usuario, Livro
#importando o form
from django import forms

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome_completo', 'email', 'telefone', 'cpf', 'data_nascimento', 'senha']
        

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome_completo', 'email', 'telefone', 'cpf', 'data_nascimento', 'senha']

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'editora', 'ano']