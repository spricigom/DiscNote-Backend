from rest_framework.serializers import ModelSerializer

from core.models import Resenha


class ResenhaSerializer(ModelSerializer):
    class Meta:
        model = Resenha
        fields = '__all__'