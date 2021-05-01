from django.shortcuts import render
from django.http import request
from rest_framework import status
import json

from .models import Produto, Estoque

# Create your views here.

def cadastro(request):
    return render(request, 'cadastro.html')
