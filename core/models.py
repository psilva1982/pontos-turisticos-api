from django.db import models

from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from localizacoes.models import Endereco

# Create your models here.
class PontoTuristico(models.Model):
    
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao, blank=True)
    comentarios = models.ManyToManyField(Comentario, blank=True)
    avaliacoes = models.ManyToManyField(Avaliacao, blank=True)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, 
        null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Ponto Turístico'
        verbose_name_plural = 'Pontos Turísticos'
