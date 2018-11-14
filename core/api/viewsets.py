from rest_framework import viewsets

from core.api.serializers import PontoTuristicoSerializer
from core.models import PontoTuristico


# ViewSets define the view behavior.
class PontoTuristicoViewSet(viewsets.ModelViewSet):
    
    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
