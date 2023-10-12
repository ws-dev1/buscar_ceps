from django.shortcuts import render, redirect
import requests

# Create your views here.

def index(request):
    return render(request, 'index.html ')

def buscar(request):
    qtd_erro = 0
    caracteres_especiais = ['!','@','#','$','%','&','*']
    if "buscar" in request.GET:
        numero_cep = request.GET['buscar']
    

    if "-" in numero_cep:
        numero_cep = numero_cep.replace('-', '')
        numero_cep = numero_cep.split()
        print(numero_cep)
        
    url_cep = f'https://viacep.com.br/ws/{numero_cep[0]}/json/'
    request_cep= requests.get(url_cep)
    dados_cep = request_cep.json()

    print(dados_cep)
    
    return render(request, 'buscar.html', {'dados': dados_cep})
