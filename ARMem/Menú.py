import time as t
import ARMem.Niveles as Niveles

black   = "\033[0;30m"
red     = "\033[0;31m"
green   = "\033[0;32m"
yellow  = "\033[0;33m"
white   = "\033[0;37m"
nocolor = "\033[0m"
blue    = "\033[0;34m"

listaJugadores=[]
def nuevoJugador(jugador:str)-> None:
    """_summary_
    Args:
        jugador (str): _description_
    """
    listaJugadores.append((jugador))
    return listaJugadores

def menuJuego():
  while True:    
    print (chr(27) + "[2J")
    print (blue)
    print ("1) Para agregar un nuevo jugador")
    print ("2) Para empezar")
    opt= input("Digite alguna de las opciones anteriores: ")
    if int(opt) == 1:
       registroJugador()
    elif int(opt) == 2: 
      if listaJugadores:
          Niveles.primerNivel()


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
menuJuego()

