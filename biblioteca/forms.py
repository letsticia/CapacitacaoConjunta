from .models import Usuario
#importando o form
from django import forms

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome_completo', 'email', 'telefone', 'cpf', 'data_nascimento', 'senha']
