from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente, GiftCard
from .forms import FormularioCliente

def lista_clientes(request) : 
    num_visitas = request.session.get('num_visitas', 1)
    num_visitas = num_visitas + 1
    request.session['num_visitas'] = num_visitas
    lista = Cliente.objects.all() 
    return render(request, 'PaginaWebApp/lista_clientes.html', 
          {'lista' : lista, 'num_visitas' : num_visitas})

def lista_giftcards(request) :
    giftcards = GiftCard.objects.all()
    return render(request, 'PaginaWebApp/lista_giftcards.html', 
           {'listaGiftcards' : giftcards})

def giftcards_saldo(request) :
    giftcards = GiftCard.objects.filter(saldoDisponible__gte=1)
    return render(request, 'PaginaWebApp/lista_giftcards.html', 
           {'listaGiftcards' : giftcards})
    
def cliente_nuevo(request) :
    if request.method == 'POST' :
        formulario = FormularioCliente(request.POST) 
        if formulario.is_valid() :
            persona = formulario.save(commit=False)
            persona.save() 
            return HttpResponse('Registro exitoso')
    else :
        formulario = FormularioCliente()
    return render(request, 'PaginaWebApp/cliente_nuevo.html', {'form' : formulario})
