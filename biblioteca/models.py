from django.db import models

# Create your models here.
class Gerente(models.Model):
    nome_completo = models.CharField(max_length=120)
    email = models.EmailField()
    cpf = models.CharField(max_length=11)
    senha = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nome_completo


class Fucionario(models.Model):
    nome_completo = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    cidade_estado = models.CharField(max_length=255, default="Cidade/Estado")
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField()
    senha = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nome_completo

class Usuario(models.Model):
    nome_completo = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    cidade_estado = models.CharField(max_length=255, default="Cidade/Estado")
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField()
    senha = models.CharField(max_length=255)

    def __str__(self):
        return self.nome_completo
    
class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    editora = models.CharField(max_length=100)
    ano = models.IntegerField()
    disponivel = models.BooleanField(default="Disponível")
    
    def __str__(self):
        return self.titulo
    
class Emprestimo(models.Model):
    
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_emprestimo = models.DateField()
    data_devolucao = models.DateField()
    status = models.BooleanField(default="Ativo")
    
    def __str__(self):
        return f'{self.livro}, emprestado para {self.usuario}'