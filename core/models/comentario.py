from django.db import models

from .resenha import Resenha


class Comentario(models.Model):
    texto = models.CharField(min_length=1,max_length=250, null=True, blank=True)
    resenha = models.ForeignKey(Resenha, on_delete=models.PROTECT, related_name="livros", null=True, blank=True)
    def __str__(self):
        return f"{Resenha.titulo}"