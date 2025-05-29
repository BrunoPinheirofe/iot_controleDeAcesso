# gestao_acesso/urls.py
from django.urls import path
from .views import VerificarAcessoView

urlpatterns = [
    path('verificar-acesso/', VerificarAcessoView.as_view(), name='verificar_acesso'),
]
