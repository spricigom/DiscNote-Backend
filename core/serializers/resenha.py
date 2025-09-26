from rest_framework.serializers import ModelSerializer, SerializerMethodField
from core.models import Resenha, Curtida


class ResenhaSerializer(ModelSerializer):
    curtidas_count = SerializerMethodField()  

    class Meta:
        model = Resenha
        fields = '__all__' 
        depth = 1

    def get_curtidas_count(self, obj):
        return obj.Curtida_resenha.count()
