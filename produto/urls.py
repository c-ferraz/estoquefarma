from django.urls import path, include
from . import views

app_name = 'produto'

urlpatterns = [
    path('cadastro', views.cadastro, name='cadastro')
]