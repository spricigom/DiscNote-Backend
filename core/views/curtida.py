from rest_framework.viewsets import ModelViewSet

from core.models import Curtida
from core.serializers import CurtidaSerializer


class CurtidaViewSet(ModelViewSet):
    queryset = Curtida.objects.all()
    serializer_class = CurtidaSerializer