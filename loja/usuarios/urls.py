from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/', views.usuarios, name='usuarios'),
    path('cadastro/', views.usuarioCadastro, name='usuarioCadastro'),
    path('setUsuario/', views.setUsuario, name='setUsuario'),
    path('atualizarInfectado/', views.atualizarInfectado, name='atualizarInfectado'),
    path('avisar/', views.avisar, name='avisar'),
    path('trocar/', views.trocar, name='trocar'),
    path('atualizarTroca/', views.atualizarTroca, name='atualizarTroca'),
    path('atualizarLocal/', views.atualizarLocal, name='atualizarLocal'),
]
