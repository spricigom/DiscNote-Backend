from django.db import models

from django.conf import settings 



class Resenha(models.Model):
    musica_id = models.TextField(null=False, blank=False)  
    texto = models.CharField(null=True, blank=True)
    nota = models.DecimalField(max_digits=2, decimal_places=1, default=5.0)
    usuario = models.ForeignKey("User", on_delete=models.CASCADE, related_name="resenhas")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.musica_id} - {self.usuario.username} - {self.nota}"
