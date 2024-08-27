from django.shortcuts import render
from django.http import HttpResponse #es la clase que response un html en el navegador. El request cuando el cliente manda algo, cuando el servidor responde es response.

# Create your views here.

def index(request):
    html="""
    <h1>Soy el index de la app1</h1>
    <h2>Hola!</h2>
    """
    return HttpResponse(html)


def jonyto(request):
    html="""
    <h1>Hola jonyto!</h1>
    <body style="color: purple">Lo amo mucho</body>
    """
    return HttpResponse(html)