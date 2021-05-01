from django.shortcuts import render
from django.http import request
from rest_framework import status
import json

from .models import Produto, Estoque

# Create your views here.

def login(request):

    response = {}

    if request.method=="POST":
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        if (usuario == 'useradm' and senha == '123456'):
            return render(request, 'inicial.html')

    return render(request, 'index.html')



def inicio(request):
    return render(request, 'inicial.html')

def index(request):
    return render(request, 'index.html')



###################################

def cadastrar_produto(request):

    if (request.method == "POST"):
        produto = Produto()
        produto.codigo_de_barras = request.POST.get('codBarraProduto')
        produto.nome_do_produto = request.POST.get('nomeProduto')
        produto.lote = request.POST.get('loteProduto')

        produto.save()

        return render(request, 'inicial.html')
