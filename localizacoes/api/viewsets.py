from rest_framework import viewsets

from localizacoes.api.serializers import EnderecoSerializer
from localizacoes.models import Endereco

class LocalizacaoViewSet(viewsets.ModelViewSet):

    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer