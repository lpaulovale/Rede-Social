from django.db import models

class Usuario(models.Model):
     nome = models.CharField(default='', max_length=100)
     idade = models.IntegerField(default=0)
     sexo = models.CharField(default='', max_length=20)
     longitude = models.CharField(default='', max_length=40)
     latitude = models.CharField(default='', max_length=40)
     aviso = models.IntegerField(default=0)
     infectado = models.BooleanField(default = False)
     #agua
     descricao1 = models.CharField(default ='Água', max_length=100)
     quantidade1 = models.IntegerField(default=0)
     pontos1 = models.IntegerField(default = 4)
     #alimentação
     descricao2 = models.CharField(default ="Alimentação", max_length=100)
     quantidade2 = models.IntegerField(default=0)
     pontos2 = models.IntegerField(default = 3)
     #medicação
     descricao3 = models.CharField(default ="Medicação", max_length=100)
     quantidade3 = models.IntegerField(default=0)
     pontos3 = models.IntegerField(default = 2)
     #munição
     descricao4 = models.CharField(default = "Munição", max_length=100)
     quantidade4 = models.IntegerField(default=0)
     pontos4 = models.IntegerField(default=1)
