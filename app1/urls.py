from django.urls import path
from . import views #para poder traer las vistas y decir que están en ese archivo.

urlpatterns = [
    path('inicio/', views.index), #la primera parte es el enlace.
    path('jonyto/', views.jonyto),
]