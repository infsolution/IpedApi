from rest_framework.validators import UniqueValidator

from rest_framework import serializers
from api.models import *




class PadariaSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	class Meta:
		model = Padaria
		fields=('url', 'pk', 'nome', 'endereco', 'latitude','longitude' ,'owner', 'produtos')

class UserCreateSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=User
		fields=('pk', 'username', 'email', 'password')

class UserSerializer(serializers.ModelSerializer):
	padarias = PadariaSerializer(many=True, read_only=True)
	class Meta:
		model= User
		fields=('url', 'username', 'padarias')

class ProdutoSerializer(serializers.HyperlinkedModelSerializer):
	padaria = serializers.SlugRelatedField(queryset=Padaria.objects.all(), slug_field='nome')
	class Meta:
		model = Produto
		fields=('url', 'nome', 'padaria', 'descricao','fabricacao', 'preco', 'foto')

class ItemSerializer(serializers.HyperlinkedModelSerializer):
	venda = serializers.SlugRelatedField(queryset=Venda.objects.all(), slug_field='pk')
	produto =serializers.SlugRelatedField(queryset=Produto.objects.all(), slug_field='pk')
	class Meta:
		model=Item
		fields=('url','venda', 'produto', 'quantidade')

class VendaSerializer(serializers.HyperlinkedModelSerializer):
	padaria = serializers.SlugRelatedField(queryset=Padaria.objects.all(), slug_field='nome')
	usuario = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
	itens =ItemSerializer(many=True, read_only=True)
	class Meta:
		model = Venda
		fields=('url', 'pk', 'padaria', 'usuario', 'valor', 'closed', 'dateFinish', 'itens')

class CloseVendaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=Venda
		fields=('pk','closed','dateFinish')

class FavoritePadaria(serializers.HyperlinkedModelSerializer):
	#favoritos = serializers.SlugRelatedField(queryset=Padaria.objects.all(), slug_field='favoritos')
	favoritos = ItemSerializer(many=True, read_only=True)
	class Meta:
		model=User
		fields=('pk', 'favoritos')