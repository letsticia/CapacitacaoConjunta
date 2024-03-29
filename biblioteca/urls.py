from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('cadastro', cadastro, name='cadastro'),
    path('login', login, name='login'),
    path('login_funcionario', login_funcionario, name='login_funcionario'),
    path('login_usuario', login_usuario, name='login_usuario'),
    path('realizar_emprestimo', realizar_emprestimo, name='realizar_emprestimo'),
    path('menu_emprestimo', menu_emprestimos, name='menu_emprestimo'),
    path('menu_funcionario', menu_funcionario, name='menu_funcionario'),
    path('cadastrar_livro', cadastrar_livro, name='cadastrar_livro'),
    path('buscar_livro', buscar_livro, name='buscar_livro'),
    path('deletar_livro', deletar_livro, name='deletar_livro'),
    path('deletar_usuario', deletar_usuario, name='deletar_usuario'),
]