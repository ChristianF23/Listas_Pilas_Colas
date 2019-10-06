import unittest
from ListaEncadenada import ListaEncadenada


class TestLista_Encadenada(unittest.TestCase):

    def test_agregar(self):
        elemento = "Hola mundo"
        tamanoEsperado = 10

        lista = ListaEncadenada()
        for i in range(10):
            lista.agregar(elemento)
        self.assertEquals(lista.tamano, tamanoEsperado)

        elemento_recibido = lista.elemento_en(9)
        self.assertEquals(elemento, elemento_recibido)

        self.assertRaises(IndexError, lista.elemento_en, 11)

    def test_quitar_longitud(self):
        lista = ListaEncadenada()
        for i in range(5):
            lista.agregar(i)
        lista.quitar(3)

        longitud_esperada = 4
        longitud_real = lista.tamano
        self.assertEquals(longitud_esperada, longitud_real)


    def test_quitar_indice(self):
        lista = ListaEncadenada()
        for i in range(5):
            lista.agregar(i)
        lista.quitar(3)

        indice_esperado = -1
        indice_real = lista.index_of(3)
        self.assertEquals(indice_esperado, indice_real)

    def test_quitar_elemento(self):
        lista = ListaEncadenada()
        for i in range(5):
            lista.agregar(i)

        elemento_esperado = 3
        elemento_real = lista.quitar(3)
        self.assertEquals(elemento_esperado, elemento_real)

    def test_quitar_enlace(self):
        lista = ListaEncadenada()
        for i in range(5):
            lista.agregar(i)
        lista.quitar(3)

        indice_esperado = 3
        indice_real = lista.index_of(4)
        self.assertEquals(indice_esperado, indice_real)

    def test_quitar_vacia(self):
        lista = ListaEncadenada()
        lista.quitar(3)

        indice_esperado = -1
        indice_real = lista.index_of(4)
        self.assertEquals(indice_esperado, indice_real)

    def test_rep(self):
        lista = ListaEncadenada()
        for i in range(5):
            lista.agregar(i)

        lista_esperada = [0, 1, 2, 3, 4]
        lista_real = lista.__repr__()
        self.assertEqual(lista_esperada, lista_real)

    def test_editar(self):
        lista = ListaEncadenada()
        for i in range(5):
            lista.agregar(i)

        nuevo_elemento = 10
        indice = 3
        lista.editar(indice, nuevo_elemento)
        elemento_real = lista.elemento_en(indice)
        self.assertEquals(elemento_real, nuevo_elemento)

    def test_editar_error(self):
        lista = ListaEncadenada()
        for i in range(5):
            lista.agregar(i)

        nuevo_elemento = 10
        indice = 30
        self.assertRaises(IndexError,lista.editar, indice, nuevo_elemento)



    def test_index_of(self):
        elemento = "prueba"

        lista = ListaEncadenada() #Elemento queda agregado
        lista.agregar(elemento)
        index_of_esperado = 0
        index_obtenido = lista.index_of(elemento)
        self.assertEqual(index_obtenido, index_of_esperado)

        for i in range (50):
            lista.agregar(f'Elemento {i}')
        index_of_esperado = 26

        index_obtenido = lista.index_of(f'Elemento {25}')
        self.assertEqual(index_obtenido, index_of_esperado)

        index_of_esperado = -1
        index_obtenido = lista.index_of('Miller')
        self.assertEqual(index_obtenido, index_of_esperado)

    def test_elemento_en(self):
        lista = ListaEncadenada()
        for i in range(1000):
            lista.agregar(i)

        elemento_esperado = 200
        elemento_real = lista.elemento_en(200)
        self.assertEquals(elemento_esperado, elemento_real)

    def test_elemento_en_error(self):
        lista = ListaEncadenada()
        for i in range(10):
            lista.agregar(i)

        indice_prueba =100
        self.assertRaises(IndexError,lista.elemento_en, indice_prueba)

if __name__ == "__main__":
    unittest.main()