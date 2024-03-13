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
    """_summary_
    Args:
        jugador (str): _description_
    """
    listaJugadores.append([jugador])
    return listaJugadores

def menuJuego():
  while True:    
    print (chr(27) + "[2J")
    print (blue)
    print ("A) Para agregar un nuevo jugador")
    print ("B) Para empezar")
    opt= input("Digite alguna de las opciones anteriores: ")
    if opt.lower() == "a":
       registroJugador()
    elif opt.lower() == "b": 
      validacion= len(listaJugadores)
      if validacion > 0:
          N.primerNivel()
      elif validacion == 0:
          print (chr(27) + "[2J")
          print("Por favor ingrese al menos un jugador antes de empezar")
          t.sleep(2)
    elif opt.lower() != "a" and opt.lower() != "b" :
       print (chr(27) + "[2J")
       print("Por favor ingrese una opción válida")
       t.sleep(2)
      
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


