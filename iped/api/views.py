
from rest_framework import status, generics, serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.shortcuts import render
from api.permissions import *
from api.serializer import *
from api.models import *
from decimal import *
from datetime import datetime
from django.utils import timezone

class PadariaList(generics.ListCreateAPIView):
	queryset = Padaria.objects.all()
	serializer_class = PadariaSerializer
	name = 'padaria-list'
	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

class PadariaDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Padaria.objects.all()
	serializer_class = PadariaSerializer
	permission_classes =(IsOwnerOrReadOnly, IsAuthenticated,)
	name='padaria-detail'


class UserCreate(generics.CreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserCreateSerializer
	permission_classes = (IsAny,)
	name='user-create'
	def perform_create(self, serializer):
		user=User.objects.create_user(serializer.data['username'], serializer.data['email'], serializer.data['password'])
		serializer.data['pk']=user.id
		return Response(serializer.data)

class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	name = 'user-list'

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	name = 'user-detail'	
	
class ProdutoList(generics.ListCreateAPIView):
	queryset = Produto.objects.all()
	serializer_class = ProdutoSerializer
	name = 'produto-list'
class ProdutoDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Produto.objects.all()
	serializer_class = ProdutoSerializer
	name='produto-detail'	
class VendaList(generics.ListCreateAPIView):
	queryset =Venda.objects.all()
	serializer_class = VendaSerializer
	name='Venda-list'
class VendaDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Venda.objects.all()
	serializer_class = VendaSerializer
	name='venda-detail'
		
class ItemList(generics.ListCreateAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer
	name='item-list'
	def perform_create(self, serializer):
		venda = Venda.objects.get(id=self.request.POST.get('venda'))
		produto = Produto.objects.get(id=self.request.POST.get('produto'))
		quantidade = Decimal(self.request.POST.get('quantidade'))
		venda.valor += (produto.preco * quantidade) 
		venda.save()
		serializer.save()


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer
	name='item-detail'
class CloseVenda(generics.UpdateAPIView):
	queryset = Venda.objects.all()
	serializer_class = CloseVendaSerializer
	name='close-venda'
	def perform_update(self, serializer):
		dateFinish = timezone.make_aware(datetime.now(),timezone.get_current_timezone())
		serializer.save(dateFinish=dateFinish)

class FavoritePadaria(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = FavoritePadaria
	name='favorite-list'
class FavoritePadariaDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = FavoritePadaria
	name='favorite-detail'