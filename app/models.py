from django.db import models

# Create your models here.
class Livros(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    quantidade = models.IntegerField(blank=True, null=True)
    disponivel = models.BooleanField(blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)

