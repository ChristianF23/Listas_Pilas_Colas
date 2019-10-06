import unittest
from ListaCircular import ListaCircular

if __name__ == '__main__':
    unittest.main()

class TestListaCircular(unittest.TestCase):
    def test_agregar_tamano(self):
        lista = ListaCircular()
        for numero in range(5):
            lista.agregar(numero)
        tamanoEsperado = 5
        tamanoObtenido = lista.tamano
        self.assertEqual(tamanoEsperado, tamanoObtenido)

    def test_agregar_primerElemento(self):
        lista = ListaCircular()
        for numero in range(5):
            lista.agregar(numero)
        elementoEsperado = 0
        elementoObtenido = lista.primero.elemento
        self.assertEqual(elementoEsperado, elementoObtenido)

    def test_agregar_ultimoElemento(self):
        lista = ListaCircular()
        for numero in range(5):
            lista.agregar(numero)
        elementoEsperado = 4
        elementoObtenido = lista.ultimo.elemento
        self.assertEqual(elementoEsperado, elementoObtenido)

    def test_quitar_tamano(self):
        lista = ListaCircular()
        for i in range(5):
            lista.agregar(i)
        lista.quitar(3)
        tamanoEsperado = 4
        tamanoObtenido = lista.tamano
        self.assertEqual(tamanoEsperado, tamanoObtenido)

    def test_quitar_elemento(self):
        lista = ListaCircular()
        for i in range(5):
            lista.agregar(i)
        elementoEsperado = 3
        elementoObtenido = lista.quitar(3)
        self.assertEqual(elementoEsperado, elementoObtenido)

    def test_indexOf_elementoExistente(self):
        lista = ListaCircular()
        for i in range(5):
            lista.agregar(i)
        indiceEsperado = 4
        indiceObtenido = lista.indexOf(4)
        self.assertEqual(indiceEsperado, indiceObtenido)

    def test_indexOf_elementoInexsistente(self):
        lista = ListaCircular()
        for i in range(5):
            lista.agregar(i)
        indiceEsperado = -1
        indiceObtenido = lista.indexOf(10)
        self.assertEqual(indiceEsperado, indiceObtenido)

    def test_elementoEn_indiceDentroLista(self):
        lista = ListaCircular()
        for i in range(5):
            lista.agregar(i)
        elementoEsperado = 2
        elementoObtenido = lista.elementoEn(2)
        self.assertEqual(elementoEsperado, elementoObtenido)

    def test_elementoEn_indiceFueraLista(self):
        lista = ListaCircular()
        for i in range(5):
            lista.agregar(i)
        indicePrueba = -1
        self.assertRaises(IndexError, lista.elementoEn, indicePrueba)

    def test_editar_valor(self):
        lista = ListaCircular()
        for i in range(5):
            lista.agregar(i)
        lista.editar(3,10)
        elementoEsperado = 10
        elementoObtenido = lista.elementoEn(3)
        self.assertEqual(elementoEsperado, elementoObtenido)