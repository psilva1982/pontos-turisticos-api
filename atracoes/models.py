from django.db import models

# Create your models here.
class Atracao(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    horario_funcionamento = models.TextField()
    idade_minima = models.IntegerField()

    class Meta:
        verbose_name = 'Atração'
        verbose_name_plural = 'Atrações'
    
    def __str__(self):
        return self.nome