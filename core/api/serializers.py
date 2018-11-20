from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

import atracoes
from atracoes.api.serializers import AtracaoSerializer
from atracoes.models import Atracao
from core.models import PontoTuristico
from localizacoes.api.serializers import EnderecoSerializer


class PontoTuristicoSerializer(serializers.ModelSerializer):
    '''
    many=True - apenas para relacionamentos muitos para muitos
    read_only=True - no momento da criação do objeto não será necessário enviar o JSON da propriedade atracoes
    '''
    atracoes = AtracaoSerializer(many=True) 
    endereco = EnderecoSerializer()
    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'aprovado', 'foto', 
            'atracoes', 'comentarios', 'avaliacoes', 'endereco', 
            'descricao_completa')
        
        read_only_fields = ('comentarios', 'avaliacoes')
    
    def cria_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)

    def create(self, validated_data):
        atracoes = validated_data['atracoes']
        del(validated_data['atracoes'])
        ponto = PontoTuristico.objects.create(**validated_data)
        self.cria_atracoes(atracoes, ponto)

        return ponto


    def get_descricao_completa(self, obj):
        return '%s - %s'  %(obj.nome, obj.descricao)
