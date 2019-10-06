class Nodo:

    elemento = None
    siguiente = None
    anterior = None

    def __init__(self, elemento, siguiente):
        self.elemento = elemento
        self.siguiente = siguiente

class Cola:
    tamano = 0
    inicioCola = None
    finCola = None

    def colaVacia(self):
        return True if self.tamano == 0 else False

    def desencolar(self):
        if self.colaVacia():
            elementoInicioCola = None
        else:
            elementoInicioCola = self.inicioCola.elemento
            self.inicioCola = self.inicioCola.siguiente
            self.tamano -= 1
        return elementoInicioCola


    def encolar(self, elemento):
        nuevoNodo = Nodo(elemento, None)
        if self.tamano == 0:
            self.inicioCola = nuevoNodo
        else:
            self.finCola.siguiente = nuevoNodo
        self.finCola = nuevoNodo
        self.tamano += 1


    def __repr__(self):
        resultado = []
        auxiliar = self
        while not auxiliar.colaVacia():
            resultado.append(auxiliar.desencolar())
        return str(resultado)