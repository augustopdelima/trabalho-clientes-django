from django.shortcuts import render
from .models import Cliente
from django.db.models.functions import Lower


def index(request):
    return render(request, "clientes/index.html")


def cliente(request):
    lista_cliente = Cliente.objects.all()
    dados_cliente = {
        'clientes': lista_cliente,
    }

    return render(request, "clientes/cliente.html", dados_cliente)


def detalhe_cliente(request, id_cliente):
    dados_cliente = Cliente.objects.get(id=id_cliente)
    dados = {
        'cliente': dados_cliente
    }

    return render(request, "clientes/detalhe_cliente.html", dados)
