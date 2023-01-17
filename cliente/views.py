from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Pessoa
from .forms import PessoaForm

def index(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'pessoas/index.html', {'pessoas': pessoas})

def adicionar(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pessoa adicionada com sucesso')
            return redirect('index')
    form = PessoaForm()
    return render(request, 'pessoas/adicionar.html', {'form': form})
    
def editar(request, id):
    pessoa = get_object_or_404(Pessoa, pk=id)
    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pessoa editada com sucesso')
            return redirect('index')
    else:
        form = PessoaForm(instance=pessoa)
    return render(request, 'pessoas/editar.html', {'form': form})
    
def excluir(request, id):
    get_object_or_404(Pessoa, pk=id).delete()
    messages.success(request, 'Pessoa removida com sucesso')
    return redirect('index')
    
    
    
    
    
    
    