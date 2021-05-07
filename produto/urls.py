from django.urls import path, include
from . import views

app_name = 'produto'

urlpatterns = [
    path('login', views.login, name='login'),
    path('inicio', views.inicio, name='inicio'),
    path('index', views.index, name='index'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('cadastrar_produto', views.cadastrar_produto, name='cadastrar_produto'),
    path('alocar', views.alocar, name='alocar_produto'),
    path('consultar', views.consultar_produto, name='consultar_produto'),
    path('editar/<int:product_id>', views.editar, name='editar'),
    path('editar_dados_produto', views.editar_dados_produto, name='editar_dados_produto'),
    path('alocar_produto', views.alocar_produto, name='alocar__produto'),
    path('desalocar', views.desalocar, name='desalocar'),
    path('editar_estoque/<int:estoque_id>', views.editar_estoque, name='editar_estoque'),
    path('desalocar_produto', views.desalocar_produto, name='desalocar_produto'),
    path('deletar_produto/<int:product_id>', views.deletar_produto, name="deletar_produto"),

]