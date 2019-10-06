from ListaAbstracta import ListaAbstracta


class Nodo:
    """
    Representa un nodo para la lista encadenada
    """

    elemento = None
    siguiente = None

    def __init__(self, elemento, siguiente):
        self.elemento = elemento
        self.siguiente = siguiente

class ListaEncadenada(ListaAbstracta):

    Primero = None
    tamano = 0
    Ultimo = None

    def agregar(self, Elemento):
        """
        O(n)
        :param Elemento:
        :return:
        """
        nuevo = Nodo(Elemento, None)
        if self.tamano == 0:
            self.Primero = nuevo
        else:
            self.Ultimo.siguiente = nuevo
        self.Ultimo = nuevo
        self.tamano += 1


    def quitar(self, Elemento):
        anterior = None
        auxiliar = self.Primero
        while auxiliar != None:
            siguiente = auxiliar.siguiente
            if auxiliar.elemento == Elemento:
                anterior.siguiente = siguiente
                self.tamano -=1
                return auxiliar.elemento
            anterior = auxiliar
            auxiliar = siguiente


    def editar(self, index, Elemento):
        if index >= self.tamano:
            raise IndexError(f'{index} esta fuera del rango de la lista')
        aux = self.Primero
        for i in range (index):
            aux = aux.siguiente
        aux.elemento = Elemento

    def index_of(self, Elemento):
        indexVar = -1

        nodoIndex = self.Primero
        for i in range (self.tamano):
            if nodoIndex.elemento == Elemento:
                indexVar = i
                return indexVar
            else:
                nodoIndex = nodoIndex.siguiente
        return indexVar

    def elemento_en(self, index):
        if index >= self.tamano:
            raise IndexError(f'{index} esta fuera del rango de la lista')
        nodoBuscado = self.Primero
        for i in range(index):
            nodoBuscado = nodoBuscado.siguiente
        return nodoBuscado.elemento


    def __repr__(self):
        listaRep = []
        aux = self.Primero
        while aux != None:
            listaRep.append(aux.elemento)
            aux = aux.siguiente
        return listaRep