from django.db import models

from .resenha import Resenha


class Comentario(models.Model):
    texto = models.CharField(max_length=250, null=True, blank=True)
    resenha = models.ForeignKey(Resenha, on_delete=models.PROTECT, related_name="Comentario_resenha")

    def __str__(self):
        return self.resenha.titulo
