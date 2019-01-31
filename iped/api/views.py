from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework import status, generics, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import *
from api.serializer import *
from api.permissions import *

class PadariaList(generics.ListCreateAPIView):
	queryset = Padaria.objects.all()
	serializer_class = PadariaSerializer
	name = 'padaria-list'
	permission_classes = (
		permissions.IsAuthenticatedOrReadOnly,
		IsOwnerOrReadOnly,)
	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

class PadariaDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Padaria.objects.all()
	serializer_class = PadariaSerializer
	name='padaria-detail'
'''class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	name = 'user-list'

class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	name = 'user-detail'''

class UserList(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	def perform_create(self, serializer):
		user = User(username=self.request.POST['username'],
					email=self.request.POST['email'])
		user.save()
		user.set_password(self.request.POST['password'])
		user.save()
	name = 'user-list'

@api_view(['POST'])
def user_create(request):
	if request.method == 'POST':
		user = User.objects.create_user(request.POST['username'],
			request.POST['email'], request.POST['password'])
		return Response(status=status.HTTP_201_CREATED)
	return Response(status=status.HTTP_400_BAD_REQUEST)	

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
