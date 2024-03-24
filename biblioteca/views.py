from django.shortcuts import render, redirect
from .forms import UsuarioForm, FuncionarioForm
from .models import Fucionario
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'main.html')

def cadastro(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UsuarioForm()
    return render(request, 'cadastro_user.html', {'form': form})

def cadastro_funcionario(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = FuncionarioForm()
    return render(request, 'cadastro_funcionario.html', {'form': form})

def login(request):
    return render(request, 'login.html')

def login_funcionario(request):
    print(request.method)
    if request.method == 'POST':
        cpf = request.POST['cpf']
        password = request.POST['password']
        
        user = authenticate(request, username=cpf, password=password)
        funcionarios = Fucionario.objects.all()
        
        for funcionario in funcionarios:
            if funcionario.cpf == cpf and funcionario.senha == password:
                print("Logado com sucesso")
                return render(request, 'main.html')
            else:
                user = None

        if user is None:
            print("Login inválido")
            messages.error(request, 'CPF ou senha inválidos.')
            return render(request, 'login_funcionario.html')
    return render(request, 'login_funcionario.html')