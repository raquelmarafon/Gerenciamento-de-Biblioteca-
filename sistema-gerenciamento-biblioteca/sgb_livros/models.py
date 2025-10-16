from django.db import models

# Create your models here.
class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=150)
    ano_publicacao = models.PositiveIntegerField()
    editora = models.CharField(max_length=100, blank=True, null=True)
