#print("Lista_jugadores.py: ",__name__)
#import Lista_jugadores



blue    = "\033[0;34m"

def registroJugador():
    while True:    
      print(blue)

      jugador=str(input("Inserte el nombre de un nuevo jugador o iniciar para empezar"))
      if jugador == str:
        Lista_jugadores.nuevoJugador(jugador)
      elif jugador.lower == "iniciar":
        break
    print (chr(27) + "[2J")
    print(Lista_jugadores.listaJugadores)

#def ingresoJugador():
 #  jugador.append(opt)
