print("Lista_jugadores.py: ",__name__)
import lista_jugadores
blue    = "\033[0;34m"

def registroJugador():
    while True:    
      print(blue)
      #print ("Inserte el nombre de un nuevo jugador")
      #print("Inserte iniciar para emepzar el juego")
      opt=str(input("Inserte el nombre de un nuevo jugador o iniciar para empezar"))
      if opt == str:
        ingresoJugador()
      elif opt.lower == "iniciar":
        break
    print (chr(27) + "[2J")
    
def ingresoJugador():
   jugador.append(opt)
