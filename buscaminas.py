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

def imprimirTableroConBombas(numeroBombas, tablero, bombas):
   for i in range(numeroBombas):
      x=bombas[i][0]
      y=bombas[i][1]
      tablero[x][y]='*'
   imprimirTablero(tablero)


def estaVaciaUnaCasilla(tablero,x,y):
   if tablero[x][y]==' ':
      return True
   else:
      return False

def colocarBombas(numeroBombas):
   bombas=[]
   for i in range(numeroBombas):
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
      if distanciaABomba(tablero, bombas, x, y)==0:
         almacenarDistancia(tablero, bombas, x, y)
         rellenarCercanas(tablero, bombas, x, y)
      elif distanciaABomba(tablero, bombas, x, y)==1:
         almacenarDistancia(tablero, bombas, x, y)
         

def juego():
   print("Bienvenido al juego de buscaminas")
   while True:
      dificultad=input("¿Qué dificultad quieres? (1, 2, 3, 4, 5): ")
      if dificultad=='1':
         numeroBombas=8
         break
      elif dificultad=='2':
         numeroBombas=15
         break
      elif dificultad=='3':
         numeroBombas=25
         break
      elif dificultad=='4':
         numeroBombas=40
         break
      elif dificultad=='5':
         numeroBombas=80
         break
      else:
         print("Esa opción no existe")

   tablero=crearTablero()
   bombas=colocarBombas(numeroBombas)
   imprimirTablero(tablero)
   while True:
      print("Quieres colocar una bandera? (s/n)")
      respuesta=input()
      if respuesta=='s':
         print("Escribe las coordenadas de la bandera")
         while True:
            x=int(input("x: ")) - 1
            y=int(input("y: ")) - 1
            if estaVaciaUnaCasilla(tablero,x,y):
               tablero[x][y]='F'
               imprimirTablero(tablero)
               break
            else:
               print("Ya hay una bandera en esa casilla")

      else:
         print("Ingrese la coordenada de la casilla")
         while True:
            x=int(input("x: ")) - 1
            y=int(input("y: ")) - 1
            if 0<=x<9 and 0<=y<9:
               break
            else:
               print("Ingrese una coordenada valida")
         if (x,y) in bombas:
            imprimirTableroConBombas(numeroBombas, tablero, bombas)
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