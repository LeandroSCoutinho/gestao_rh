from django.views.generic import ListView
from .models import Funcionario

class FuncionarioList(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada=self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)