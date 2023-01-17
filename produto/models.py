from django.db import models
from sorl.thumbnail import ImageField
        
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(decimal_places=2, max_digits=7)
    estoque = models.IntegerField()
    imagem = models.ImageField(upload_to='produto')
    
    def __str__(self):
        return f'{self.nome}'
