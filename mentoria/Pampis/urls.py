from django.urls import path
from Pampis import views

urlpatterns = [
    path("", views.special, name ="index"),
    #path("special/", views.special, name = 'special'),
    #path("index/", views.index, name ="index"),
]
