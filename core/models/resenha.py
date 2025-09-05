from django.db import models

from django.conf import settings 



class Resenha(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.CharField(null=True, blank=True)
    usuario = models.ForeignKey("User", on_delete=models.CASCADE, related_name="resenhas")


    def __str__(self):
        return f"{self.titulo}"
