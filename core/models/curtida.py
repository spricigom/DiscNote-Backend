from django.db import models

from django.conf import settings 

from .resenha import Resenha


class Curtida(models.Model):
    curtida = models.BooleanField()
    resenha = models.ForeignKey(Resenha, on_delete=models.PROTECT, related_name="Curtida_resenha", null=True, blank=True)
    usuario = models.ForeignKey("User", on_delete=models.CASCADE, related_name="curtidas")

    def __str__(self):
        return f"{Resenha.titulo}"
