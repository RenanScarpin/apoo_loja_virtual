from django.db import models

# Define os atributos da classe produto que serão salvos no banco de dados
class Produto(models.Model):
    nome = models.CharField(max_length=100) # Tamanho máximo do campo de 100 caracteres
    descricao = models.TextField() # Representa um texto sem limite fixo de tamanho
    preco = models.DecimalField(max_digits=10, decimal_places=2) # Número decimal com no máximo 10 dígitos, e 2 casas decimais
    quantidade = models.PositiveIntegerField()
    imagem = models.ImageField(upload_to='produtos/', null=True, blank=True) # Campo para upload de imagem
    data_cadastro = models.DateTimeField(auto_now_add=True) 

    def __str__(self): # Define como o objeto será representado como string
        return self.nome
