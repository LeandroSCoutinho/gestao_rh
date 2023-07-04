from django.urls import path
from .views import DocumentoNovo


urlpatterns = [
    path('novo/<int:funcionario_id>/',DocumentoNovo.as_view(), name = 'create_documento' ),
   # path('delete/<int:pk>',DocumentoDelete.as_view(), name = 'delete_documento' ),
]