from django.urls import path
from inicio import views

urlpatterns = [
    path("", views.special, name ="special"),
    path("", views.aluno, name = 'aluno'),
    path("<slug:chave>", views.navegar, name = 'navegar'),
    path("usuario/<slug:chave>", views.viajar, name = 'viajar'),
    #path('paisagem', views.paisagem, name ="paisagem"),

    #path("index/", views.index, name ="index"),
]
