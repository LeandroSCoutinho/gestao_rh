from django.db import models
from django.shortcuts import reverse
from apps.funcionarios.models import Funcionario


class Documento(models.Model) :
    descricao = models.CharField(max_length=120)
    pertence = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    arquivo = models.FileField(upload_to='documentos')

    def get_absolute_url(self):
        return  reverse('edit_funcionario', args=[self.pertence.id])

    def __str__(self):
        return self.descricao