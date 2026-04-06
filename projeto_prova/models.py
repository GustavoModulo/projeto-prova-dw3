from django.db import models
from django.contrib.auth.models import AbstractUser

# Tabela de Usuário
class Usuario(AbstractUser):
    pass

# Tabela de Funcionário
class Funcionario(models.Model):
    cpf = models.CharField(max_length=14)
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    remuneracao = models.DecimalField(max_digits=10, decimal_places=2)
    tempo_de_servico = models.IntegerField()

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"

# Tabela de Produto
class Produto(models.Model):
    descricao = models.CharField(max_length=255)
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

# Tabela de Venda
class Venda(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Venda {self.id} - Funcionario: {self.funcionario.nome}"