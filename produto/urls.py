from django.urls import path, include
from . import views

app_name = 'produto'

urlpatterns = [
    path('login', views.login, name='login'),
    path('inicio', views.inicio, name='inicio'),
    path('index', views.index, name='index'),
    path('cadastrar_produto', views.cadastrar_produto, name='cadastrar_produto'),
    path('alocar', views.alocar, name='alocar_produto'),
    path('consultar', views.consultar_produto, name='consultar_produto'),
    path('editar/<int:product_id>', views.editar, name='editar'),
    path('editar_dados_produto', views.editar_dados_produto, name='editar_dados_produto'),

]