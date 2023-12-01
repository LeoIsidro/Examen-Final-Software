import unittest
import requests

class TestAPI(unittest.TestCase):
    def test_contactos_1(self):
        # Se realiza un caso de prueba para el end point /billetera/contactos se envia un numero de cuenta que existe
        response = requests.post('http://127.0.0.1:5000/billetera/contactos?minumero=21345')
        self.assertEqual(response.status_code, 200)

        # Se realiza un caso de prueba para el end point /billetera/pagar se envia un numero de cuenta que no existe
    def test_contactos_2(self):
        response = requests.post('http://127.0.0.1:5000/pagar?minumero=2134&numerodestino=125&valor=100')
        self.assertEqual(response.status_code, 404)

        # Se realiza un caso de prueba para el end point /billetera/pagar se envia un valor mayor al saldo
    def test_contactos_3(self):
        response = requests.post('http://127.0.0.1:5000/pagar?minumero=21345&numerodestino=123&valor=300')
        self.assertEqual(response.status_code, 404)

        # Se realiza un caso de prueba para el end point /billetera/historial se envia un numero de cuenta que no existe
    def test_contactos_4(self):
        response = requests.post('http://127.0.0.1:5000/billetera/historial?minumero=1234')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()