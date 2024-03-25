from django.shortcuts import render, redirect
from .forms import UsuarioForm, FuncionarioForm
from .models import Fucionario, Usuario, Livro, Emprestimo
from django.contrib.auth import authenticate, login
from django.contrib import messages

def index(request):
    return render(request,'main.html')

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        cidade_estado = request.POST.get('cidade')
        cpf = request.POST.get('cpf')
        datanascimento = request.POST.get('datanascimento')
        idade = request.POST.get('idade')
        instituicao = request.POST.get('instituicao')
        senha = request.POST.get('senha')
        
        if nome == '' or email == '' or telefone == '' or cidade_estado == '' or cpf == '' or datanascimento == '' or idade == '' or instituicao == '' or senha == '':
            messages.error(request, 'Preencha todos os campos.')
            return render(request, 'cadastro_usuario.html')
        else:
            usuario = Usuario(nome_completo = nome, email = email, telefone = telefone, cidade_estado = cidade_estado, cpf = cpf, data_nascimento = datanascimento, idade = idade, instituicao = instituicao, senha = senha)
            usuario.save()
            return render(request, 'main.html')
    return render(request, 'cadastro_user.html')

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

def menu_emprestimos(request):
    return render(request, 'menu_emprestimo.html')

def realizar_emprestimo(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        livro = request.POST.get('livro')
        cpf = request.POST.get('cpf')
        senha = request.POST.get('senha')
        
        if nome == '' or livro == '' or cpf == '' or senha == '':
            messages.error(request, 'Preencha todos os campos.')
            return render(request, 'realizar_emprestimo.html')
        else:
            usuario = Usuario.objects.filter(nome_completo = nome, cpf = cpf, senha = senha)
            livro = Livro.objects.filter(titulo = livro)
            
            if len(usuario) == 0 or len(livro) == 0:
                messages.error(request, 'Usuário ou livro não encontrado.')
                return render(request, 'realizar_emprestimo.html')
            else:
                from datetime import datetime, timedelta

                data_emprestimo = datetime.now()

                data_devolucao = data_emprestimo + timedelta(days=15)

                data_emprestimo_str = data_emprestimo.strftime('%d/%m/%Y')
                data_devolucao_str = data_devolucao.strftime('%d/%m/%Y')
                
                livro.update(disponivel = False)
                
                emprestimo = Emprestimo(livro = livro[0], usuario = usuario[0], data_emprestimo = data_emprestimo_str, data_devolucao = data_devolucao_str)
                emprestimo.save()
                
                return render(request, 'menu_funcionarios.html')
    return render(request, 'realizar_emprestimo.html')

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
            livro = Livro(titulo = nome, autor = autor, editora = editora, ano = ano, disponivel = True)
            livro.save()
            return render(request, 'menu_funcionarios.html')

    return render(request, 'cadastrar_livro.html')

def buscar_livro(request):
    
    if request.method == 'POST':
        nome = request.POST.get('nome')
        autor = request.POST.get('autor')
        editora = request.POST.get('editora')
        ano = request.POST.get('ano')
    
        if nome == '' or autor == '' or editora == '' or ano == '':
            messages.error(request, 'Preencha todos os campos.')
            return render(request, 'buscar_livro.html')
        else:
            livros = Livro.objects.filter(titulo = nome, autor = autor, editora = editora, ano = ano)
            
            if len(livros) == 0:
                messages.error(request, 'Livro não encontrado.')
                return render(request, 'buscar_livro.html')
            else:
                messages.success(request, 'Livro encontrado.')
                return render(request, 'menu_funcionarios.html')
        
    return render(request, 'buscar_livro.html')

def deletar_livro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        autor = request.POST.get('autor')
        editora = request.POST.get('editora')
        ano = request.POST.get('ano')
    
        if nome == '' or autor == '' or editora == '' or ano == '':
            messages.error(request, 'Preencha todos os campos.')
            return render(request, 'deletar_livro.html')
        else:
            livros = Livro.objects.filter(titulo = nome, autor = autor, editora = editora, ano = ano)
            
            if len(livros) == 0:
                messages.error(request, 'Livro não encontrado.')
                return render(request, 'deletar_livro.html')
            else:
                livros.delete()
                messages.success(request, 'Livro deletado.')
                return render(request, 'menu_funcionarios.html')
                
    return render(request, 'deletar_livro.html')

def deletar_usuario(request):
    return render(request, 'deletar_user.html')