from django.db import models

# Create your models here.
class Endereco(models.Model):
    linha1 = models.CharField(max_length=150)
    linha2 = models.CharField(max_length=150, null=True, blank=True)
    cidade = models.CharField(max_length=150)
    estado = models.CharField(max_length=70)
    estado = models.CharField(max_length=70)
    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

    def __str__(self):
        return self.linha1 + ' ' + self.linha2
    
    