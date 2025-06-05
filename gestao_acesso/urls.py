# gestao_acesso/urls.py
from django.urls import path
from .views import VerificarAcessoView, CadastrarCartaoView
from django.views.generic import RedirectView

urlpatterns = [
    path('verificar-acesso/', VerificarAcessoView.as_view(), name='verificar_acesso'),
    path('cadastrar-card/<int:usuario_id>/', CadastrarCartaoView.as_view()),
    
]
