from django.urls import path
from produto.views import *

urlpatterns = [
	path('', IndexView.as_view(), name='produto_index'),
    path('adicionar/', ProdutoCreateView.as_view(), name='produto_adicionar'),
    path('remover/<int:pk>', ProdutoDeleteView.as_view(), name='produto_apagar'),
    path('editar/<int:pk>', ProdutoEditView.as_view(), name='produto_editar'),
]