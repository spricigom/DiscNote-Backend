from django.db import models


class Resenha(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.CharField(min_length=1, null=True, blank=True)

    def __str__(self):
        return f"{self.titulo}"