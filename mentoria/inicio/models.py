from django.db import models

# Create your models here.

class dados_usuario(models.Model):
    nome_a = models.CharField(max_length=20)
    nascimento_a = models.DateField(auto_now=False, auto_now_add=False)
    email_a = models.EmailField(max_length=254)
    senha_a = models.CharField(max_length=15)

class agendas(models.Model):
    pendencia_a = models.CharField(max_length=50)
    inicio_a = models.DateTimeField(auto_now=False, auto_now_add=False) 
    fim_a = models.DateTimeField(auto_now=False, auto_now_add=False) 

class fotog(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=250, blank=False)
    foto = models.FileField()




