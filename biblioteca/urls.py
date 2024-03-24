from django.urls import path
from .views import index, cadastro, login, login_funcionario, login_usuario

urlpatterns = [
    path('', index, name='index'),
    path('cadastro', cadastro, name='cadastro'),
    path('login', login, name='login'),
    path('login_funcionario', login_funcionario, name='login_funcionario'),
    path('login_usuario', login_usuario, name='login_usuario'),
]