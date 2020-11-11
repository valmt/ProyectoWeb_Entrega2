from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_clientes, name='lista_clientes'),
    path('cliente/nuevo', views.cliente_nuevo, name='cliente_nuevo'),
    path('giftcards', views.lista_giftcards, name='lista_giftcards'),
    path('tarjetas_saldo', views.giftcards_saldo, name='giftcards_saldo'),    
]
    