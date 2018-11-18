from rest_framework import request, viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter

from core.api.serializers import PontoTuristicoSerializer
from core.models import PontoTuristico


# ViewSets define the view behavior.
class PontoTuristicoViewSet(viewsets.ModelViewSet):

   serializer_class = PontoTuristicoSerializer
   filter_backends = (SearchFilter,)
   search_fields = ('nome','descricao', 'endereco__linha1')

   def get_queryset(self):

      # Filtrando por querystring
      # ao invés de utilizar query_params['id'] que lançará exceção caso o parametro não seja passado
      id = self.request.query_params.get('id', None) 
      nome = self.request.query_params.get('nome', None)
      descricao = self.request.query_params.get('descricao', None)
      
      queryset = PontoTuristico.objects.all()

      if id:
       queryset = queryset.filter(pk=id)
      
      if nome:
         queryset = queryset.filter(nome__icontains=nome)
      
      if descricao:
         queryset = queryset.filter(descricao=descricao)

      return queryset
   
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
