'''from django.test import TestCase

from django.test import Client

c = Client()'''
#response = c.get('/usuarios/')
#print(response.status_code)
'''response = c.post('/setUsuario/', {nome:'Paulo', idade:56, sexo:'masculino', longitude:'50 graus', 
latitude:'46 graus L', aviso:0, infectado:False, quantidade1:2, quantidade2:2, quantidade3:2, quantidade4:2})
print(response.status_code)'''

import unittest
from django.test import Client

class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_details(self):
        # Issue a GET request.
        response = self.client.get('/usuarios/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

  