from ListaAbstracta import ListaAbstracta

class Nodo:

    elemento = None
    siguiente = None

    def __init__(self, elemento, siguiente):
        self.elemento = elemento
        self.siguiente = siguiente

class ListaCircular(ListaAbstracta):
    tamano = 0
    primero = None
    ultimo = None

    def agregar(self, elemento):
        if self.tamano == 0:
            elementoAuxiliar = Nodo(elemento, None)
            self.primero = elementoAuxiliar
        else:
            elementoAuxiliar = Nodo(elemento, None)
            self.ultimo.siguiente = elementoAuxiliar
        self.ultimo = elementoAuxiliar
        self.ultimo.siguiente = self.primero
        self.tamano += 1

    def quitar(self, elemento):
        nodoAuxiliar = self.primero
        nodoAnterior = self.ultimo
        for i in range(self.tamano):
            if nodoAuxiliar.elemento == elemento:
                if self.tamano == 1:
                    self.primero = None
                    self.ultimo = None
                else:
                    nodoAnterior.siguiente = nodoAuxiliar.siguiente
                self.tamano -= 1
                return nodoAuxiliar.elemento
            nodoAuxiliar = nodoAuxiliar.siguiente
            nodoAnterior = nodoAnterior.siguiente

    def indexOf(self, elemento):
        indice = -1
        contador = 0
        nodoAuxiliar = self.primero
        for i in range(self.tamano):
            if nodoAuxiliar.elemento == elemento:
                indice = contador
                break
            contador += 1
            nodoAuxiliar = nodoAuxiliar.siguiente
        return indice

    def elementoEn(self, indice):
        if indice < 0 or indice >= self.tamano:
            raise IndexError(f'{indice} esta fuera del rango de la lista')
        contador = 0
        nodoAuxiliar = self.primero
        for i in range(indice+1):
            if contador == indice:
                return nodoAuxiliar.elemento
            contador += 1
            nodoAuxiliar = nodoAuxiliar.siguiente
        return indice

    def editar(self, indice, elemento):
        if indice < 0 or indice >= self.tamano:
            raise IndexError(f'{indice} esta fuera del rango de la lista')
        contador = 0
        nodoAuxiliar = self.primero
        for i in range(indice+1):
            if contador == indice:
                nodoAuxiliar.elemento = elemento
                break
            contador += 1
            nodoAuxiliar = nodoAuxiliar.siguiente