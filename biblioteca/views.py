from django.shortcuts import render, redirect
from .forms import UsuarioForm, FuncionarioForm

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
    return render(request, 'login_funcionario.html')