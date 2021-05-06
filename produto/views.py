from django.shortcuts import render
from django.http import request, HttpResponseRedirect
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

def alocar(request):

    return render(request, 'alocar.html')

def consultar_produto(request):

    produtos = Produto.objects.all()

    contexto = {
        'produtos': produtos
    }

    return render(request, 'consultar.html', contexto)

def editar(request, product_id):

    if request.method == 'GET':
        produtos = Produto.objects.filter(codigo_de_barras=product_id)
        contexto = {
            'produtos': produtos
        }
    return render(request, 'editar.html', contexto)

def editar_dados_produto(request):

    if request.method == 'POST':
        nome_do_produto = request.POST.get('nomeProduto')
        codigo_de_barras = request.POST.get('codBarraProduto')
        lote = request.POST.get('loteProduto')
        ativo = request.POST.get('ativoProduto')
        product_id = request.POST.get('product_id')

        if ativo != None:
            ativo = True
        else:
            ativo = False

        produto = Produto.objects.filter(codigo_de_barras=product_id)
        produto.update(nome_do_produto=nome_do_produto, codigo_de_barras=codigo_de_barras, lote=lote, ativo=ativo)

    return HttpResponseRedirect('/produto/inicio')
