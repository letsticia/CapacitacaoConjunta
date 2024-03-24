from django.urls import path
from .views import index, cadastro, login, login_funcionario

urlpatterns = [
    path('', index, name='index'),
    path('cadastro', cadastro, name='cadastro'),
    path('login', login, name='login'),
    path('login_funcionario', login_funcionario, name='login_funcionario'),
]