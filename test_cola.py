import unittest
from Cola import Cola


class TestCola(unittest.TestCase):

    def test_encolar_tamano(self):
        cola = Cola()
        for unidad in range(10):
            cola.encolar(unidad)
        tamanoEsperado = 10
        tamanoObtenido = cola.tamano
        self.assertEqual(tamanoEsperado, tamanoObtenido)

    def test_encolar_inicio(self):
        cola = Cola()
        for unidad in range(10):
            cola.encolar(unidad)
        inicioColaEsperado = 0
        inicioColaObtenido = cola.desencolar()
        self.assertEqual(inicioColaEsperado, inicioColaObtenido)

    def test_encolar_fin(self):
        cola = Cola()
        for unidad in range(10):
            cola.encolar(unidad)
        finColaEsperado = 9
        finColaObtenido = cola.finCola.elemento
        self.assertEqual(finColaEsperado, finColaObtenido)

    def test_colaVacia(self):
        cola = Cola()
        self.assertTrue(cola.colaVacia())
        elemento = 1
        cola.encolar(elemento)
        self.assertFalse(cola.colaVacia())

    def test_desencolar(self):
        cola = Cola()
        for unidad in range(10):
            cola.encolar(unidad)
        elementoEsperado = 0
        elementoObtenido = cola.desencolar()
        self.assertEqual(elementoEsperado, elementoObtenido)
        for unidad in range(3):
            cola.desencolar()
        elementoEsperado = 4
        elementoObtenido = cola.desencolar()
        self.assertEqual(elementoEsperado, elementoObtenido)

    def test_cola_representacion(self):
        cola = Cola()
        for numero in range(1, 11):
            cola.encolar(numero)
        representacionEsperada = str([1,2,3,4,5,6,7,8,9,10])
        representacionObtenida = cola.__repr__()
        self.assertEqual(representacionEsperada, representacionObtenida)


if __name__ == "__main__":
    unittest.main()




