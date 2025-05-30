from django.db import models

from .resenha import Resenha


class Curtida(models.Model):
    curtida = models.BooleanField()
    resenha = models.ForeignKey(Resenha, on_delete=models.PROTECT, related_name="livros", null=True, blank=True)
    def __str__(self):
        return f"{Resenha.titulo}"