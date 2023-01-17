from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(verbose_name='Nome', max_length=100)
    idade = models.IntegerField(verbose_name='Idade')
    endereco = models.CharField(verbose_name='Endereço', max_length=100)
    altura = models.FloatField(verbose_name='Altura')
    data_nascimento = models.DateField(verbose_name='Data de Nascimento', null=True)
    
    def __str__(self):
        return f"{self.nome}"
