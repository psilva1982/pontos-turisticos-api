from rest_framework import viewsets

from atracoes.api.serializers import AtracaoSerializer
from atracoes.models import Atracao

class AtracaoViewSet(viewsets.ModelViewSet):

    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer