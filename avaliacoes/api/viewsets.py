from avaliacoes.api.serializers import AvalizacaoSerializer
from rest_framework import viewsets

from avaliacoes.models import Avaliacao


class AvaliacaoViewSet(viewsets.ModelViewSet):

    queryset = Avaliacao.objects.all()
    serializer_class = AvalizacaoSerializer
