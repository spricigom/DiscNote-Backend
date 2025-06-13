from django.db import models

from .resenha import Resenha


class Curtida(models.Model):
    curtida = models.BooleanField()
    resenha = models.ForeignKey(Resenha, on_delete=models.PROTECT, related_name="Curtida_resenha")

    def __str__(self):
        return self.resenha.titulo
