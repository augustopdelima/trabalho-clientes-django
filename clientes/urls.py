from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cliente/', views.cliente, name='cliente'),
    path('detalhe_cliente/<id_cliente>',
         views.detalhe_cliente, name='detalhe_cliente')
]
