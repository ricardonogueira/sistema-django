from django.contrib import admin
from cliente.models import Pessoa

class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'endereco', 'altura', 'data_nascimento',)

admin.site.register(Pessoa, PessoaAdmin)
