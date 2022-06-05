from core.models import Animal
from core.serializers import AnimalSerializer
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)


class AnimalListView(ListCreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer


class AnimalDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
