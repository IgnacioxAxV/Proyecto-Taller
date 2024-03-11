import time as t
import Lista_jugadores

black   = "\033[0;30m"
red     = "\033[0;31m"
green   = "\033[0;32m"
yellow  = "\033[0;33m"
white   = "\033[0;37m"
nocolor = "\033[0m"
blue    = "\033[0;34m"

#listaJugadores=[]
def menuJuego():
  while True:    
    print (chr(27) + "[2J")
    print (blue)
    print ("Desea ingresar nuevo jugador?")
    print (green)
    print ("si para ingresar nuevo judador")  
    print (red)
    print ("no para empezar juego")
    print (white)
    opt= str(input("Digite alguna de las opciones anteriores: "))
    if opt == "si":
       registroJugador()
    elif opt == "no":
       break
  print (chr(27) + "[2J")

def registroJugador():   
  print (chr(27) + "[2J")
  while True:
    jugador=str(input ("Ingrese nombre del jugador o salir para cancelar:"))
    if jugador.lower() == "salir":
      break
    elif jugador != "salir":
      Lista_jugadores.nuevoJugador(jugador)

  print(Lista_jugadores.listaJugadores)
  t.sleep(5)
       
menuJuego()