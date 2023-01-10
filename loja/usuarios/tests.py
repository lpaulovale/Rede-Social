import unittest
from django.test import TestCase
from django.test import Client
from usuarios.models import Usuario

class SimpleTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        arg = Usuario.objects.create(nome='Pedro', idade=56, sexo='masculino', longitude='50 graus', 
                          latitude='46 graus L', aviso=0, infectado=False, quantidade1=2, quantidade2=2, 
                          quantidade3=2, quantidade4=2)        

    def test_details(self):
    
        response = self.client.get('/usuarios/')
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(response.context['nome'], "Paulo")