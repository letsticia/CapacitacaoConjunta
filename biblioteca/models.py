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
    nome_completo = models.CharField(max_length=120)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    senha = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nome_completo

class Usuario(models.Model):
    nome_completo = models.CharField(max_length=120)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    cpf = models.CharField(max_length=11)
    idade = models.IntegerField()
    instituicao = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    endereço = models.CharField(max_length=100)
    senha = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nome_completo
    
class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    editora = models.CharField(max_length=100)
    ano = models.IntegerField()
    genero = models.CharField(max_length=100)
    status = models.BooleanField(default="Disponível")
    
    def __str__(self):
        return self.titulo
    
class Emprestimo(models.Model):
    id_emprestimo = models.IntegerField()
    id_livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_emprestimo = models.DateField()
    data_devolucao = models.DateField()
    status = models.BooleanField(default="Ativo")
    
    def __str__(self):
        return f'{self.id_livro}, emprestado para {self.id_usuario}'