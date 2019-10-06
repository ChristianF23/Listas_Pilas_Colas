from ListaAbstracta import ListaAbstracta

class Nodo:

    elemento = None
    siguiente = None
    anterior = None

    def __init__(self, elemento, siguiente, anterior):
        self.elemento = elemento
        self.siguiente = siguiente
        self.anterior = anterior

class ListaDoblementeCircular(ListaAbstracta):
    tamano = 0
    primero = None
    ultimo = None


    def agregar(self, elemento):
        elementoAuxiliar = Nodo(elemento, self.primero, self.ultimo)
        if self.tamano == 0:
            self.primero = elementoAuxiliar
            self.primero.siguiente = elementoAuxiliar
            self.primero.anterior = elementoAuxiliar
        else :
            self.ultimo.siguiente = elementoAuxiliar
        self.ultimo = elementoAuxiliar
        self.tamano += 1

    def quitar(self, elemento):
        nodoAuxiliar = self.primero
        for i in range(self.tamano):
            if nodoAuxiliar.elemento == elemento:
                if nodoAuxiliar.siguiente != None:
                    nodoAuxiliar.siguiente.anterior = nodoAuxiliar.anterior
                if nodoAuxiliar.anterior != None:
                    nodoAuxiliar.anterior.siguiente = nodoAuxiliar.siguiente
                self.tamano -= 1
                return nodoAuxiliar.elemento
            nodoAuxiliar = nodoAuxiliar.siguiente
        return nodoAuxiliar

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
        for i in range(indice + 1):
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
        for i in range(indice + 1):
            if contador == indice:
                nodoAuxiliar.elemento = elemento
                break
            contador += 1
            nodoAuxiliar = nodoAuxiliar.siguiente
