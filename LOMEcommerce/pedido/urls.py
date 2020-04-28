from django.urls import path
from . import views

app_name = 'pedido'  # pedido:pagar

urlpatterns = [
    path('', views.Pagar.as_view(), name='pagar'),
    path('fecharpedido/', views.FecharPedido.as_view(), name='fecharpedido'),
    path('detalhe/', views.Detalhe.as_view(), name='detalhe'),
]
