from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='pessoa_index'),
    path('adicionar', views.adicionar, name='pessoa_adicionar'),
    path('editar/<int:id>', views.editar, name='pessoa_editar'),
    path('excluir/<int:id>', views.excluir, name='pessoa_excluir'),
]