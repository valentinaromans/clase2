from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    html=("""
          <h1>Soy el index de la app2</h1>
          """)
    return HttpResponse

def saludo(request):
    html=("""
        <h1>Hola</h1>
        <a href="/app2/index">Volver</a>
    """)
    return HttpResponse
