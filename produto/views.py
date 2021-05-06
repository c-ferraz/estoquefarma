from django.shortcuts import render
from django.http import HttpResponseRedirect
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


def cadastro(request):
    return render(request, 'cadastro.html')


def alocar(request):
    return render(request, 'alocar.html')


def consultar(request):
    return render(request, 'consultar.html')


def atualizar(request):
    return render(request, 'atualizar.html')


###################################

def cadastrar_produto(request):

    if (request.method == "POST"):
        produto = Produto()
        produto.codigo_de_barras = request.POST.get('codBarraProduto')
        produto.nome_do_produto = request.POST.get('nomeProduto')
        produto.lote = request.POST.get('loteProduto')

        produto.save()

        contexto = {
            'response': status.HTTP_201_CREATED
        }

        return render(request, 'cadastro.html', contexto)


def alocar_produto(request):
    if (request.method == 'POST'):
        alocar = Estoque()
        try:
            produto = Produto.objects.get(codigo_de_barras=request.POST.get('codBarraProduto'))
        except:
            contexto = {
                'response': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': 'O produto informado não foi encontrado no banco de dados.'
            }
            return render(request, 'alocar.html', contexto)
        alocar.codigo_de_barras = produto
        alocar.pratileira = request.POST.get('localProduto')
        alocar.quantidade = request.POST.get('quantidadeProduto')
        alocar.dt_validade = request.POST.get('validadeProduto')

        alocar.save()

        contexto = {
            'code': status.HTTP_201_CREATED
        }
    else:
        contexto = {
            'code': status.HTTP_400_BAD_REQUEST
        }

    return render(request, 'alocar.html', contexto)


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

    return HttpResponseRedirect('/produto/consultar')


def desalocar(request):

    estoque = Estoque.objects.all()

    contexto = {
        "estoque": estoque
    }
    return render(request, 'desalocar.html', contexto)


def editar_estoque(request, estoque_id):
    if request.method == 'GET':
        estoque = Estoque.objects.filter(id=estoque_id)

        contexto = {
            "estoque": estoque
        }
    return render(request, 'editar_estoque.html', contexto)


def desalocar_produto(request):
    if request.method == 'POST':
        local = request.POST.get('localEstoque')
        quantidade = request.POST.get('quantidadeEstoque')
        validade = request.POST.get('validadeEstoque')
        estoque_id = request.POST.get('estoque_id')

        estoque = Estoque.objects.filter(id=estoque_id)
        estoque.update(pratileira=local, quantidade=quantidade, dt_validade=validade)

    return HttpResponseRedirect('/produto/desalocar')