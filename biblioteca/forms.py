from django.forms import ModelForm
from .models import Usuario, Funcionario, Livro, Emprestimo

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome_completo', 'email', 'telefone', 'cpf', 'idade', 'instituicao', 'data_nascimento', 'endereço', 'senha']

class FuncionarioForm(ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome_completo', 'email', 'telefone', 'cidade', 'estado', 'cpf', 'data_nascimento', 'senha']

class LivroForm(ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'editora', 'ano', 'genero', 'status']

class EmprestimoForm(ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['livro', 'usuario', 'data_emprestimo', 'data_devolucao', 'status']