from django.test import TestCase
from .rutificador import validar_rut

class TestValidadoresChilenos(TestCase):

    def test_rut_valido(self):
        rut = "16628475-9"
        resultado = validar_rut(rut)
        self.assertTrue(resultado)
    
    def test_rut_incorrecto(self):
        rut = "16628475-8"
        resultado = validar_rut(rut)
        self.assertFalse(resultado)

    def test_rut_formato_erroneo(self):
        rut = "16628475-8-2"
        resultado = validar_rut(rut)
        self.assertFalse(resultado)

    def test_texto_en_vez_de_rut(self):
        rut = "Hola mundo!"
        resultado = validar_rut(rut)
        self.assertFalse(resultado)
    
    def test_rut_conK(self):
        rut = "19912756-K"
        resultado = validar_rut(rut)
        self.assertTrue(resultado)

    def test_rut_conk(self):
        rut = "19912756-k"
        resultado = validar_rut(rut)
        self.assertTrue(resultado)
   
 
