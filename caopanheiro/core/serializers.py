from core.models import Animal
from rest_framework.serializers import ModelSerializer


class AnimalSerializer(ModelSerializer):
    class Meta:
        model = Animal
        fields = "__all__"
        read_only_fields = ["criado_em", "atualizado_em"]
