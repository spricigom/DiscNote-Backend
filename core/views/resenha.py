from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from django.db.models import Avg

from core.models import Resenha
from core.serializers import ResenhaSerializer


class ResenhaViewSet(ModelViewSet):
    queryset = Resenha.objects.all()
    pagination_class = None
    serializer_class = ResenhaSerializer

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

    @action(detail=False, methods=['get'], url_path='musica/(?P<musica_id>[^/.]+)')
    def resenhas_musica(self, request, musica_id=None):
        """
        Retorna a média de nota e total de resenhas para uma música (musica_id).
        """
        qs = self.queryset.filter(musica_id=musica_id)
        media_nota = qs.aggregate(Avg('nota'))['nota__avg'] or 0
        total_resenhas = qs.count()
        return Response({
            'media_nota': round(media_nota, 1),
            'total_resenhas': total_resenhas
        })
