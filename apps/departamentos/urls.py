from django.urls import path
from .views import (
    DepartamentoList,
    DepartamentoNovo,
    DepartamentoEdit
)

urlpatterns = [
    path('',DepartamentoList.as_view(), name = 'list_departamentos' ),
    path('novo',DepartamentoNovo.as_view(), name = 'create_departamento' ),
    path('edit/<int:pk>',DepartamentoEdit.as_view(), name = 'update_departamento' ),
]