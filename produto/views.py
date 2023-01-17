from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .models import Produto
from .forms import ProdutoForm

class IndexView(ListView):
    model = Produto
    context_object_name = 'produtos'
    template_name = 'produtos/index.html'

class ProdutoCreateView(SuccessMessageMixin, CreateView):
    template_name = 'produtos/adicionar.html'
    form_class = ProdutoForm
    success_url = '/produto/'
    success_message = "Produto adicionado com sucesso"
    
class ProdutoDeleteView(SuccessMessageMixin, DeleteView):
    model = Produto
    template_name = 'produtos/produto_confirm_delete.html'
    success_url = '/produto/'
    success_message = "Produto removido com sucesso"
    
class ProdutoEditView(SuccessMessageMixin, UpdateView):
    model = Produto
    template_name = 'produtos/editar.html'
    fields = ['nome', 'preco', 'estoque', 'imagem']
    success_url = '/produto/'
    success_message = "Produto editado com sucesso"

