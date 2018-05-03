#!/usr/bin/python
# coding=utf-8
# Para poder poner acentos en comentarios
# Alberto Penhos
# A01018426
#
# Se hizo con listas, ahí se guardan los valores en el siguiente formato:
#  Posición de la lista:
#  0  3  6
#  1  4  7
#  2  5  8
#
# La meta es el estado final en el cual se requiere que este el tablero, se puede cambiar
# manteniendo el mismo formato dado.
#
#  1  2  3
#  4  5  6
#  7  8  0
#
# El 0 es para definir el espacio en blanco, donde se puede mover.
estadoFinal = [1, 4, 7, 2, 5, 8, 3, 6, 0]
#
# Al correr el programa se pedira el número en la posición del tablero indicada
# tomando la forma mencionada anteriormente

import sys


# La estructura del nodo.
class Nodo:
    def __init__(self, estado, padre, op, pro, costo):
        # El estado del nodo
        self.estado = estado
        # Es el nodo padre
        self.padre = padre
        # Contiene la operación necesaria para llegar a este desde el padre.
        self.op = op
        # Profundidad del nodo actual, padre.pro +1
        self.pro = pro
        # Contiene el costo para llegar a este nodo. No se usa para el BFS
        self.costo = costo


def tablero(estado):
    print "%i  %i  %i" % (estado[0], estado[3], estado[6])
    print "%i  %i  %i" % (estado[1], estado[4], estado[7])
    print "%i  %i  %i" % (estado[2], estado[5], estado[8])
    print ""


# Movimiento, 0 = arriba, 1 = abajo, 2 = izquierda, 3 = derecha
def movimiento(estado, dire):
    estadoN = estado[:]
    ind = estadoN.index(0)
    if dire == 0:
        # Revisamos si es posible trabajar hacia arriba, estos valores
        if ind not in [0, 3, 6]:
            # Cambiar valores
            temp = estadoN[ind - 1]
            estadoN[ind - 1] = estadoN[ind]
            estadoN[ind] = temp
            return estadoN
        else:
            # No se puede mover (None es el NULL de Python)
            return None
    elif dire == 1:
        # Revisamos si es posible trabajar hacia abajo, estos valores
        if ind not in [2, 5, 8]:
            # Cambiar valores
            temp = estadoN[ind + 1]
            estadoN[ind + 1] = estadoN[ind]
            estadoN[ind] = temp
            return estadoN
        else:
            # No se puede mover (None es el NULL de Python)
            return None
    elif dire == 2:
        # Revisamos si es posible trabajar hacia la izquierda, estos valores
        if ind not in [0, 1, 2]:
            # Cambiar valores
            temp = estadoN[ind - 3]
            estadoN[ind - 3] = estadoN[ind]
            estadoN[ind] = temp
            return estadoN
        else:
            # No se puede mover (None es el NULL de Python)
            return None
    elif dire == 3:
        # Revisamos si es posible trabajar hacia la derecha, estos valores
        if ind not in [6, 7, 8]:
            # Cambiar valores
            temp = estadoN[ind + 3]
            estadoN[ind + 3] = estadoN[ind]
            estadoN[ind] = temp
            return estadoN
        else:
            # No se puede mover (None es el NULL de Python)
            return None


def crarNodo(estado, padre, op, pro, costo):
    return Nodo(estado, padre, op, pro, costo)


def expNode(nodo, nodos):
    """Returns a list of expanded nodos"""
    expNodos = []
    expNodos.append(crarNodo(movimiento(nodo.estado, 0), nodo, "u", nodo.pro + 1, 0))
    expNodos.append(crarNodo(movimiento(nodo.estado, 1), nodo, "d", nodo.pro + 1, 0))
    expNodos.append(crarNodo(movimiento(nodo.estado, 2), nodo, "l", nodo.pro + 1, 0))
    expNodos.append(crarNodo(movimiento(nodo.estado, 3), nodo, "r", nodo.pro + 1, 0))
    # Nodos imposibles de mover se quitan (movimiento regresa None)
    expNodos = [nodo for nodo in expNodos if nodo.estado != None]  # list comprehension!
    return expNodos


def bfs(inicial, meta):
    # Hace la busqueda de inicio a meta
    # Una lista es como una cola para los nodos.
    nodos = []
    # Creamos la cola con el nodo raíz en ella.
    nodos.append(crarNodo(inicial, None, None, 0, 0))
    while True:
        # No hay solución, sin estados posibles.
        if len(nodos) == 0: return None
        # Tomamos el primer nodo, como cualquier cola FIFO.
        nodo = nodos.pop(0)
        # Agregamos el movimiento que hicimos
        # Si es la meta regresamos los movimientoes necesarios
        if nodo.estado == meta:
            moves = []
            temp = nodo
            while True:
                moves.insert(0, temp.op)
                if temp.pro == 1: break
                temp = temp.padre
            return moves
        # Trabajar el nodo y todos los resultados al frente de la pila.
        nodos.extend(expNode(nodo, nodos))


def dfs(inicial, meta, pro=10):
    # La profundidad máxima
    limiteProfundidad = pro
    nodos = []
    nodos.append(crarNodo(inicial, None, None, 0, 0))
    while True:
        # Sin solucion
        if len(nodos) == 0: return None
        nodo = nodos.pop(0)
        # Movimientos necesarios
        if nodo.estado == meta:
            moves = []
            temp = nodo
            while True:
                moves.insert(0, temp.op)
                if temp.pro <= 1: break
                temp = temp.padre
            return moves
        # Continuar si seguimos en el limite de profundidad
        if nodo.pro < limiteProfundidad:
            expNodos = expNode(nodo, nodos)
            expNodos.extend(nodos)
            nodos = expNodos


# Main method
def main():
    estadoInicial = []
    for i in range(0, 9):
        estadoInicial.append(int(raw_input('Inserta el numero ' + str(i) + ': ')))
    ### CHANGE THIS FUNCTION TO USE bfs, dfs, ids or a_star
    result = bfs(estadoInicial, estadoFinal, )
    if result == None:
        print "No existe solucion"
    elif result == [None]:
        print "El nodo inicial es la meta!"
    else:
        print result
        print len(result), " movimientos"


# Ejecutar funcion main.
if __name__ == "__main__":
    main()