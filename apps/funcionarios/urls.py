from django.urls import path
from .views import FuncionarioList, FuncionarioEdit, FuncionarioDelete

urlpatterns = [
    path('',FuncionarioList.as_view(), name = 'list_funcionarios' ),
    path('editar/<int:pk>/',FuncionarioEdit.as_view(), name = 'edit_funcionarios' ),
    path('deletar/<int:pk>/',FuncionarioDelete.as_view(), name = 'delete_funcionarios' ),
]