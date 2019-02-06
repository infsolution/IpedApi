# -*- coding: utf-8 -*-
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include
from api import views
urlpatterns = [
	path('padaria/',views.PadariaList.as_view(), name=views.PadariaList.name),#Lista e Cria padarias
	path('padaria/<int:pk>/',views.PadariaDetail.as_view(), name=views.PadariaDetail.name),#Editar, Deletar uma padaria
	path('users/',views.UserList.as_view(),name=views.UserList.name),#Lista Usuarios
	path('users/<int:pk>/',views.UserDetail.as_view(),name=views.UserDetail.name),
	path('produto/',views.ProdutoList.as_view(),name=views.ProdutoList.name),#Lista e Cria produtos
	path('produto/<int:pk>/',views.ProdutoDetail.as_view(),name=views.ProdutoDetail.name),
	path('user-create/',views.UserCreate.as_view(), name=views.UserCreate.name),#Cria Usuarios - usar este
	path('venda/', views.VendaList.as_view(), name=views.VendaList.name),#Lista e Cria vendas
	path('venda/<int:pk>/',views.VendaDetail.as_view(), name=views.VendaDetail.name),
	path('item/', views.ItemList.as_view(), name=views.ItemList.name),#Lista e adciona item na venda
	path('item/<int:pk>',views.ItemDetail.as_view(), name=views.ItemDetail.name),
	path('close-venda/<int:pk>/',views.CloseVenda.as_view(), name=views.CloseVenda.name), #Fecha uma venda
	path('favorite/', views.FavoritePadaria.as_view(), name=views.FavoritePadaria.name),
	path('favorite/<int:pk>/', views.FavoritePadariaDetail.as_view(), name=views.FavoritePadariaDetail.name),
	path('api-auth/', include('rest_framework.urls')),
	path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
]
