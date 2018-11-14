from rest_framework import viewsets

from core.api.serializers import PontoTuristicoSerializer
from core.models import PontoTuristico


# ViewSets define the view behavior.
class PontoTuristicoViewSet(viewsets.ModelViewSet):
    
   serializer_class = PontoTuristicoSerializer

   def get_queryset(self):
      
      return  PontoTuristico.objects.filter(aprovado=True)
