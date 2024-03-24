from django.shortcuts import render, redirect
from .forms import UsuarioForm, FuncionarioForm
from .models import Fucionario, Usuario, Livro
from django.contrib.auth import authenticate, login
from django.contrib import messages

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
    if request.method == 'POST':
        cpf = request.POST['cpf']
        password = request.POST['password']
        
        user = authenticate(request, username=cpf, password=password)
        funcionarios = Fucionario.objects.all()
        
        for funcionario in funcionarios:
            if funcionario.cpf == cpf and funcionario.senha == password:
                print("Logado com sucesso")
                return render(request, 'menu_funcionarios.html')
            else:
                user = None

        if user is None:
            print("Login inválido")
            messages.error(request, 'CPF ou senha inválidos.')
            return render(request, 'login_funcionario.html')
    return render(request, 'login_funcionario.html')

def login_usuario(request):
    if request.method == 'POST':
        cpf = request.POST['cpf']
        password = request.POST['password']
        
        user = authenticate(request, username=cpf, password=password)
        usuarios = Usuario.objects.all()
        print(len(usuarios))
        
        for usuario in usuarios:
            print(usuario.cpf, usuario.senha)
            if usuario.cpf == cpf and usuario.senha == password:
                return render(request, 'main.html')
            else:
                user = None

        if user is None:
            print("Login inválido")
            messages.error(request, 'CPF ou senha inválidos.')
    return render(request, 'login_usuario.html')

def menu_funcionario(request):
    return render(request, 'menu_funcionarios.html')

def realizar_emprestimo(request):
    return render(request, 'realizar_emprestimo.html')

def menu_emprestimos(request):
    return render(request, 'menu_emprestimo.html')

def cadastrar_livro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        autor = request.POST.get('autor')
        editora = request.POST.get('editora')
        ano = request.POST.get('ano')
    
        if nome == '' or autor == '' or editora == '' or ano == '':
            messages.error(request, 'Preencha todos os campos.')
            return render(request, 'cadastrar_livro.html')
        else:
            livro = Livro(titulo = nome, autor = autor, editora = editora, ano = ano, status = True)
            livro.save()

    return render(request, 'cadastrar_livro.html')