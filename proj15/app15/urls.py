"""
URL configuration for proj15 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from .views import generate_report
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('registrar_doacao/', views.registrar_doacao, name='registrar_doacao'),
    path('lista_doacoes/', views.lista_doacoes, name='lista_doacoes'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', LogoutView.as_view(next_page='register'), name='logout'),
    path('home/', views.home, name='home'),
    path('feedbackdoador/', views.feedbackdoador, name='feedbackdoador'),
    path("relatorio/", views.generate_report, name="generate_report"),
    path('necessidades-especificas/', views.necessidades_view, name='necessidades_especificas'), 
    path('faqs/', views.faq_list, name='faq_list'),
    path('faqs/<int:faq_id>/respond/', views.submit_response, name='submit_response'),
    path('perguntas-frequentes/', views.perguntas_frequentes, name='perguntas_frequentes'),
    path('enviar-pergunta/', views.enviar_pergunta, name='enviar_pergunta'),
    path('gerenciar-perguntas/', views.gerenciar_perguntas, name='gerenciar_perguntas'),
    path('historico-doacoes/', views.historico_doacoes, name='historico-doacoes'),
    path("mapeamento/", views.map_view, name="mapeamento"),
]