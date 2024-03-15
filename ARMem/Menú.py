import time as t
import Niveles as N

black   = "\033[0;30m"
red     = "\033[0;31m"
green   = "\033[0;32m"
yellow  = "\033[0;33m"
white   = "\033[0;37m"
nocolor = "\033[0m"
blue    = "\033[0;34m"

listaJugadores=[]
def nuevoJugador(jugador:str)-> None:
    listaJugadores.append([jugador])
    return listaJugadores
      
def registroJugador():   
  print (chr(27) + "[2J")
  while True:
    jugador= input("Ingrese nombre del jugador:")
    print("Inserte 'ok' para regresar al menu")
    if jugador.lower() == "ok":
      menuJuego()
    else:
      nuevoJugador(jugador)
print(listaJugadores)

def conteoFinal(l:list):
    cont=0
    for i in range(len(listaJugadores)):
        L=listaJugadores[cont]
        reporteFinal=L[1]+L[2]+L[3]
        L.append(reporteFinal)
        cont+=1
    quitarReportes(listaJugadores)
    
def quitarReportes(l:list):
    listaCopia= l.copy()
    cont= 0
    for y in range(len(listaJugadores)):
        listaCopia[cont].pop(1)
        listaCopia[cont].pop(1)
        listaCopia[cont].pop(1)
        cont+=1
    definirTop(listaCopia)

def definirTop(l:list):
    contador=0
    while(contador<len(l)-1):
        if (l[contador][1]<l[contador+1][1]):
            pass
        else:
            temporal= l[contador]
            l[contador]=l[contador+1]
            l[contador+1]=temporal
        contador+=1
    imprimirTop(l)
    
def imprimirTop(l:list):
    print (chr(27) + "[2J")
    if (len(l)>=3):
        print(red)
        print(f"El tercer lugar con un tiempo de {l[2][1]}s es para {l[2][0]}")
        t.sleep(3)
        print(f"El segundo lugar con un tiempo de {l[1][1]}s es para {l[1][0]}")
        t.sleep(3)
        print(f"El primer lugar con un tiempo de {l[0][1]}s es para {l[0][0]}")
        t.sleep(10)
    if (len(l)==2):
        print(green)
        print(f"El segundo lugar con un tiempo de {l[1][1]}s es para {l[1][0]}")
        t.sleep(3)
        print(f"El primer lugar con un tiempo de {l[0][1]}s es para {l[0][0]}")
        t.sleep(10)
    if (len(l)==1):
        print(yellow)
        print(f"El tiempo de {l[0][0]} fue de {l[0][1]}s")
        t.sleep(10)


def procesoJuego1(listaJugadores:list):
  N.ejecucionPrimerNivel(listaJugadores)
  N.ejecucionSegundoNivel(listaJugadores)
  N.ejecucionTercerNivel(listaJugadores)
  conteoFinal(listaJugadores)
  listaJugadores.clear()

def menuJuego():
  while True:    
    print (chr(27) + "[2J")
    print (blue)
    print ("A) Para agregar un nuevo jugador")
    print ("B) Para empezar")
    opcion= 0
    opcion= input("Digite alguna de las opciones anteriores: ")
    if opcion.lower() == "a":
       registroJugador()
    elif opcion.lower() == "b":
      validacion= len(listaJugadores)
      if validacion > 0:
          procesoJuego1(listaJugadores)
          menuJuego()
      elif validacion == 0:
          print (chr(27) + "[2J")
          print("Por favor ingrese al menos un jugador antes de empezar")
          t.sleep(2)
    elif opcion.lower() != "a" and opcion.lower() != "b" :
       print (chr(27) + "[2J")
       print("Por favor ingrese una opción válida")
       t.sleep(2)
   
#conteoFinal(listaJugadores)
menuJuego()