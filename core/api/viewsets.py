from rest_framework import request, viewsets
from rest_framework.decorators import action

from core.api.serializers import PontoTuristicoSerializer
from core.models import PontoTuristico


# ViewSets define the view behavior.
class PontoTuristicoViewSet(viewsets.ModelViewSet):

   queryset = PontoTuristico.objects.all() 
   serializer_class = PontoTuristicoSerializer

   #def get_queryset(self):
   #   
   #   return  PontoTuristico.objects.filter(aprovado=True)
   
   # Sobrescrevendo o método list = GET em pontosturisticos/
   def list(self, request, *args, **kwargs):
      return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

   # Sobrescrevendo o método create = PUT em pontosturisticos/
   def create(self, request, *args, **kwargs):

      # Aqui posso colocar meu código 

      # Ao final chama o comportamento padrão 
      return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

   # Sobrescrevendo o método destroy = DELETE em pontosturisticos/id
   def destroy(self, request, *args, **kwargs):
      return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)
   
   # Sobrescrevendo o método retrieve = GET em pontosturisticos/id
   def retrieve(self, request, *args, **kwargs):
      return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

   # Sobrescrevendo o método update = PUT em pontosturisticos/id
   def update(self, request, *args, **kwargs):
      return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

   # Sobrescrevendo o método partial_update = PATH em pontosturisticos/id
   def partial_update(self, request, *args, **kwargs):
      return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)

   # Criando action personalizada 
   # detail=True será necessário passar a pk 
   # /pontosturisticos/1/denunciar
   @action(methods=['get'], detail=True)   
   def denunciar(self, request, pk=None):
      pass

   # Criando uma action personalizada
   # detail=False não é necessário passar a pk 
   # atinge todo o endpoint /pontosturisticos/todoendpoint
   @action(methods=['get'], detail=False)
   def todoendpoint(self, request):
      pass
