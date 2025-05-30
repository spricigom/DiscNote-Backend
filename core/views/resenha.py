from rest_framework.viewsets import ModelViewSet

from core.models import Resenha
from core.serializers import ResenhaSerializer


class ResenhaViewSet(ModelViewSet):
    queryset = Resenha.objects.all()
    serializer_class = ResenhaSerializer