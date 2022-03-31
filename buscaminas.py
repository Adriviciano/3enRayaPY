import random

def crearTablero():
   tablero=[]
   for i in range(9):
      tablero.append([])
      for j in range(9):
         tablero[i].append(' ')
   return tablero

def imprimirTablero(tablero):
   print('-------------------------------------')
   for i in range(9):
      for j in range(9):
         if j == 0:
            print("|", tablero[i][j],end=" | ")
         else:
            print(tablero[i][j],end=" | ")
      print()
      print('-------------------------------------')

def imprimirTableroConBombas(tablero, bombas):
   for i in range(8):
      x=bombas[i][0]
      y=bombas[i][1]
      tablero[x][y]='*'
   imprimirTablero(tablero)


def estaVaciaUnaCasilla(tablero,x,y):
   if tablero[x][y]==' ':
      return True
   else:
      return False

def colocarBombas():
   bombas=[]
   for i in range(8):
      while True:
         x=random.randint(0,8)
         y=random.randint(0,8)
         if (x,y) not in bombas:
            bombas.append((x,y))
            break
   return bombas
      
def tableroLleno(tablero):
   for i in range(9):
      for j in range(9):
         if tablero[i][j]==' ':
            return False
   return True

def partidaGanada(tablero):
   for i in range(9):
      for j in range(9):
         if tablero[i][j]==' ':
            return False
   return True

def distanciaABomba(tablero, bombas, a, b):
   if tablero[a][b]==' ':
      contador=0
      for x in range(-1,2):
         for y in range(-1,2):
            if 0<=a+x<9 and 0<=b+y<9:
               if (a+x, b+y) in bombas:
                  contador+=1
      return contador

def almacenarDistancia(tablero,bombas, a, b):
   tablero[a][b] = distanciaABomba(tablero, bombas, a, b)

#una funcion casillaContigua que reciba un tablero y una coordenada y devuelva una lista con las coordenadas de las casillas contiguas
def casillaContigua(tablero, a, b):
   lista=[]
   for i in range(-1,2):
      for j in range(-1,2):
         if 0<=a+i<9 and 0<=b+j<9:
            lista.append((a+i,b+j))
   return lista


def rellenarCercanas(tablero, bombas, x, y):
   lista=casillaContigua(tablero, x, y)
   for i in range(len(lista)):
      x=lista[i][0]
      y=lista[i][1]
      if distanciaABomba(tablero, bombas, x, y)==1 or distanciaABomba(tablero, bombas, x, y)==0:
         almacenarDistancia(tablero, bombas, x, y)
         rellenarCercanas(tablero, bombas, x, y)
         

def juego():
   tablero=crearTablero()
   bombas=colocarBombas()
   imprimirTablero(tablero)
   while True:
      print("Ingrese la coordenada de la casilla")
      while True:
         x=int(input("x: ")) - 1
         y=int(input("y: ")) - 1
         if 0<=x<9 and 0<=y<9:
            break
         else:
            print("Ingrese una coordenada valida")
      if (x,y) in bombas:
         imprimirTableroConBombas(tablero, bombas)
         print('Has perdido')
         break
      else:
         if estaVaciaUnaCasilla(tablero,x,y):
            almacenarDistancia(tablero, bombas, x, y)
            rellenarCercanas(tablero, bombas, x, y)
            imprimirTablero(tablero)
            if tableroLleno(tablero):
               print("Ganaste")
               break
         else:
            print("Ya ingresaste esa casilla")

juego()