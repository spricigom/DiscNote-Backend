from django.db import models

from django.conf import settings 

from .resenha import Resenha


class Comentario(models.Model):
    texto = models.CharField(max_length=250, null=True, blank=True)
    resenha = models.ForeignKey(Resenha, on_delete=models.PROTECT, related_name="Comentario_resenha", null=True, blank=True)
    usuario = models.ForeignKey("User", on_delete=models.CASCADE, related_name="comentarios")

    def __str__(self):
        return f"{self.resenha.musica_id} - {self.usuario.username} - {self.texto}"
