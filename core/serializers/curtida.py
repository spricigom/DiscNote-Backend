from rest_framework.serializers import ModelSerializer

from core.models import Curtida


class CurtidaSerializer(ModelSerializer):
    class Meta:
        model = Curtida
        fields = '__all__'