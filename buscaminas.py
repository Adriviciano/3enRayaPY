import random
import sys

def crearTablero(tamaño):
   tablero=[]
   for i in range(tamaño):
      tablero.append([])
      for j in range(tamaño):
         tablero[i].append(' ')
   return tablero

def imprimirTablero(tablero, tamaño):
   print(' ---'*tamaño)
   for i in range(tamaño):
      for j in range(tamaño):
         if j == 0:
            print("|", tablero[i][j],end=" | ")
         else:
            print(tablero[i][j],end=" | ")
      print()
      print(' ---'*tamaño)

def imprimirTableroConBombas(numeroBombas, tablero, bombas, tamaño):
   for i in range(numeroBombas):
      x=bombas[i][0]
      y=bombas[i][1]
      tablero[x][y]='*'
   imprimirTablero(tablero, tamaño)


def estaVaciaUnaCasilla(tablero,x,y):
   if tablero[x][y]==' ' or tablero[x][y]=='F':
      return True
   else:
      return False

def colocarBombas(numeroBombas, tamaño):
   bombas=[]
   for i in range(numeroBombas):
      while True:
         x=random.randint(0,tamaño - 1)
         y=random.randint(0,tamaño - 1)
         if (x,y) not in bombas:
            bombas.append((x,y))
            break
   return bombas
      
def tableroLleno(tablero, tamaño):
   for i in range(tamaño):
      for j in range(tamaño):
         if tablero[i][j]==' ':
            return False
   return True

def partidaGanada(tablero, tamaño, bombas):
   if tableroLleno(tablero, tamaño) and soloBanderasEnBombas(tablero, tamaño, bombas):
      return True
   else:
      contador=0
      for i in range(tamaño):
         for j in range(tamaño):
            if tablero[i][j]=='F' or tablero[i][j]==' ':
               contador+=1
      if contador == len(bombas) and soloBanderasEnBombas(tablero, tamaño, bombas):
         return True
   return False

def soloBanderasEnBombas(tablero, tamaño, bombas):
   for i in range(tamaño):
      for j in range(tamaño):
         if tablero[i][j]=='F' and (i,j) not in bombas:
            return False
   return True

def distanciaABomba(tablero, bombas, a, b, tamaño):
   if tablero[a][b]==' ' or tablero[a][b]=='F':
      contador=0
      for x in range(-1,2):
         for y in range(-1,2):
            if 0<=a+x<tamaño and 0<=b+y<tamaño:
               if (a+x, b+y) in bombas:
                  contador+=1
      return contador

def almacenarDistancia(tablero,bombas, a, b, tamaño):
   tablero[a][b] = distanciaABomba(tablero, bombas, a, b, tamaño)

#una funcion casillaContigua que reciba un tablero y una coordenada y devuelva una lista con las coordenadas de las casillas contiguas
def casillaContigua(a, b, tamaño):
   lista=[]
   for i in range(-1,2):
      for j in range(-1,2):
         if 0<=a+i<tamaño and 0<=b+j<tamaño:
            lista.append((a+i,b+j))
   return lista


def rellenarCercanas(tablero, bombas, x, y, tamaño):
   lista=casillaContigua(x, y, tamaño)
   for i in range(len(lista)):
      x=lista[i][0]
      y=lista[i][1]
      if (x,y) not in bombas:
         if distanciaABomba(tablero, bombas, x, y, tamaño)==0:
            almacenarDistancia(tablero, bombas, x, y, tamaño)
            rellenarCercanas(tablero, bombas, x, y, tamaño)
         elif distanciaABomba(tablero, bombas, x, y, tamaño)==1:
            almacenarDistancia(tablero, bombas, x, y, tamaño)
         

def juego():
   print("Bienvenido al juego de buscaminas")
   while True:
      tamaño = int(input("Ingrese el tamaño del tablero (3-10): "))
      if 3<=tamaño<=10:
         break
      else:
         print("El tamaño debe estar entre 2 y 10")

   while True:
      dificultad=input("¿Qué dificultad quieres? (1, 2, 3, 4): ")
      if dificultad=='1':
         numeroBombas=tamaño - 1
         break
      elif dificultad=='2':
         numeroBombas=2 * tamaño - 2
         break
      elif dificultad=='3':
         numeroBombas=3 * tamaño - 3
         break
      elif dificultad=='4':
         numeroBombas=4 * tamaño - 4
         break
      else:
         print("Esa opción no existe")

   tablero=crearTablero(tamaño)
   bombas=colocarBombas(numeroBombas, tamaño)
   imprimirTablero(tablero, tamaño)
   while True:
      print("Quieres colocar una bandera? (s/n)")
      respuesta=input()
      if respuesta=='s':
         print("Escribe las coordenadas de la bandera")
         while True:
            x=int(input("x: ")) - 1
            y=int(input("y: ")) - 1

            if 0<=x<tamaño and 0<=y<tamaño:
               if estaVaciaUnaCasilla(tablero,x,y):
                  tablero[x][y]='F'
                  if tableroLleno(tablero, tamaño):
                     imprimirTablero(tablero, tamaño)
                     print("Ganaste")
                     sys.exit()
                  else:
                     imprimirTablero(tablero, tamaño)
                     break
               else:
                  print("Ya hay una bandera en esa casilla")
            else:
               print("Las coordenadas deben estar entre 1 y", tamaño)

      else:
         print("Ingrese la coordenada de la casilla")
         while True:
            x=int(input("x: ")) - 1
            y=int(input("y: ")) - 1
            if 0<=x<tamaño and 0<=y<tamaño:
               break
            else:
               print("Ingrese una coordenada valida")
         if (x,y) in bombas:
            imprimirTableroConBombas(numeroBombas, tablero, bombas, tamaño)
            print('Has perdido')
            break
         else:
            if estaVaciaUnaCasilla(tablero,x,y) or tablero[x][y]=='F':
               almacenarDistancia(tablero, bombas, x, y, tamaño)
               rellenarCercanas(tablero, bombas, x, y, tamaño)
               imprimirTablero(tablero, tamaño)
               if partidaGanada(tablero, tamaño, bombas):
                  print("Ganaste")
                  sys.exit()
            else:
               print("Ya ingresaste esa casilla")

juego()