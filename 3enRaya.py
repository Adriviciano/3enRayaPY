#Un 3 en raya para jugar 1v1 contra una IA, que muestre el tablero por consola

import random
import sys

def crearTablero():
    '''Crea el tablero'''
    tablero = []
    for i in range(3):
        tablero.append([' '] * 3)
    return tablero

def imprimirTablero(tablero):
    '''Imprime el tablero'''
    print()
    for i in range(3):
        print(' ' + tablero[i][0] + ' | ' + tablero[i][1] + ' | ' + tablero[i][2])
        if i != 2:
            print("-----------")
    print()

def tableroLleno(tablero):
    '''Determina si el tablero está lleno'''
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == ' ':
                return False
    return True


def movimientoJugador(tablero):
    '''Jugador 1'''
    while True:
        while True:
            fila = int(input('Ingresa la fila: '))
            if fila > 0 and fila < 4:
                break
        while True:
            columna = int(input('Ingresa la columna: '))
            if columna > 0 and columna < 4:
                break
        if tablero[fila - 1][columna - 1] == ' ':
            break
        else:
            print('Esa casilla ya está ocupada, ingresa otra')
    tablero[fila - 1][columna - 1] = 'X'

#una funcion que realice un movimiento aleatorio del jugador 2
def movimientoAleatorio(tablero):
    '''Jugador 2'''
    while True:
        fila = random.randint(0, 2)
        columna = random.randint(0, 2)
        if tablero[fila - 1][columna - 1] == ' ':
            break
    tablero[fila - 1][columna - 1] = 'O'



#una funcion que determine si alguien ha ganado, para ganar deben ser iguales las fichas de una fila, columna o cualquiera de las dos diagonales
def hayGanador(tablero, ficha):
    '''Determina si hay un ganador'''
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] == ficha:
            return True
        if tablero[0][i] == tablero[1][i] == tablero[2][i] == ficha:
            return True
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == ficha:
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == ficha:
        return True
    return False

#una funcion que comprueba que jugador es el ganador del
def quienGana(tablero, ficha):
    '''Determina quien gana'''
    if hayGanador(tablero, ficha):
        if ficha == 'X':
            return 'Jugador 1'
        else:
            return 'Jugador 2'
    else:
        pass

#el bucle de juego que incluye las funciones anteriores para
#imprimir el tablero, el movimiento del jugador y el movimiento de la IA
def jugar():
    '''Juego'''
    tablero = crearTablero()
    imprimirTablero(tablero)
    while True:
        if tableroLleno(tablero):
            print('Empate')
            break
        movimientoJugador(tablero)
        imprimirTablero(tablero)
        if quienGana(tablero, 'X'):
            print('Ganó el jugador 1')
            sys.exit()
        if tableroLleno(tablero):
            print('Empate')
            break
        print("Movimiento PC")
        movimientoAleatorio(tablero)
        imprimirTablero(tablero)
        if quienGana(tablero, 'O'):
            print('Ganó el jugador 2')
            sys.exit()

jugar()