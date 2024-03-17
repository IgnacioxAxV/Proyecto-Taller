import time as t
import Niveles as N

black   = "\033[0;30m"      #Conjunto de variables utilizadas paraa cambiar el color de las fuentes de la terminal
red     = "\033[0;31m"      #Conjunto de variables utilizadas paraa cambiar el color de las fuentes de la terminal
green   = "\033[0;32m"      #Conjunto de variables utilizadas paraa cambiar el color de las fuentes de la terminal
yellow  = "\033[0;33m"      #Conjunto de variables utilizadas paraa cambiar el color de las fuentes de la terminal
white   = "\033[0;37m"      #Conjunto de variables utilizadas paraa cambiar el color de las fuentes de la terminal
nocolor = "\033[0m"         #Conjunto de variables utilizadas paraa cambiar el color de las fuentes de la terminal
blue    = "\033[0;34m"      #Conjunto de variables utilizadas paraa cambiar el color de las fuentes de la terminal
 
listaJugadores=[]           #Lista vacía donde se colocará el nombre de jugadores y sus tiempos por nivel correspondientes

def nuevoJugador(jugador:str)-> None:
    """Función que agrega el nombre del jugador nuevo como sublista detro de una lista predefinida.

    Args:
        jugador (str): Nombre que del jugador que se otorgue a si mismo.
    """
    listaJugadores.append([jugador])
      
def registroJugador():   
    """Función que solicita y manda el nombre del usuario que se registró para si mismo en el juego 
    a una función de registro de nombre. Además de dar la opción al usuario de regresar al menu.
    """
    while True:
        print (chr(27) + "[2J")
        print(f"La lista de jugadores {listaJugadores}")
        jugador= input("Ingrese nombre del jugador:")
        if jugador.lower() == "ok":
            menuJuego()
        elif len(jugador) == 0:
            print(chr(27) + "[2J")
            print("Debe de tener al menos un carácter el nombre") 
            t.sleep(3)
        else:
            var=[jugador]
            if var in listaJugadores:
                print(chr(27) + "[2J")
                print("Este jugador ya existe, por favor ingrese un nombre distinto")
                t.sleep(3)
                registroJugador()
            else:
                print(chr(27) + "[2J")
                nuevoJugador(jugador)
                print("Si desea regresar al menu inserte 'ok'")
                t.sleep(3)
    
def conteoFinal(l:list):
    """Función que toma todos los reportes de nivel de cada jugador y los suma para crear el reporte 
    final del juego.

    Args:
        tiempoN (list): Referencia de la lista otorgada a la función.
    """
    for i in range(len(listaJugadores)):
        reporteFinal=listaJugadores[i][1]+listaJugadores[i][2]+listaJugadores[i][3]
        listaJugadores[i].append(reporteFinal)
    quitarReportes(listaJugadores)

def quitarReportes(l:list):
    """Función que realiza una copia de la lista original que posee los nombres, reportes de nivel y de reporte
    final y se eliminan los reportes de nivel. Para más adelante trabajar en la función de top jugadores e 
    imprimirlos.

    Args:
        l (list): Copia de la lista origianal
    """
    listaCopia= l.copy()
    cont= 0
    for y in range(len(listaJugadores)):
        listaCopia[y].pop(1)
        listaCopia[y].pop(1)
        listaCopia[y].pop(1)
    definirTop(listaCopia)

def definirTop(l:list):
    """Función que ordena la copia de la lista original del que tuvo el menor tiempo al que tuvo mayor tiempo
    durante la partida del juego.

    Args:
        l (list): Referencia de la lista suministrada a la función.
    """
    while True:
        cambio=False
        for e in range(len(l)-1):
            if (l[e][1]<l[e+1][1]):
                pass
            else:
                temporal= l[e]
                l[e]=l[e+1]
                l[e+1]=temporal
                cambio=True
        if cambio == False:
            break

    imprimirTop(l)
    
def imprimirTop(l:list):
    """Función que imprime el top de los tres mejores tiempos durante la partida. Además de uso de condicionales
    en el caso de que la partida haya sido jugada por dos o un jugador para la impresión del top.

    Args:
        l (list):Referencia de la lista suministrada a la función. 
    """
    print (chr(27) + "[2J")
    print("===============")
    print("Juego terminado")
    print("===============")
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

def reporteNivel1(l:list):
    """Función que define el orden de los jugadores según su tiempo en 
    el nivel 1 por medio del método de ordenamiento por burbuja.

    Args:
        l (list): lista que llega por parámetro a la función. 
    """
    listaCopia1=l.copy()
    while True:
        cambio = False
        for e in range(len(listaCopia1)-1):
            if (listaCopia1[e][1]<listaCopia1[e+1][1]):
                pass
            else :
                temporal= listaCopia1[e]
                listaCopia1[e]=listaCopia1[e+1]
                listaCopia1[e+1]=temporal
                cambio=True
        if cambio == False:
            break
    imprimirReporte1(listaCopia1)

def imprimirReporte1(l:list):
    """Función encargada de imprimir en la terminal los resultados de los mejores
    tiempos de los jugadores en el nivel 1.

    Args:
        l (list): Lista que llega por parámetro a la función.
    """
    print (chr(27) + "[2J")
    print("Nivel uno completado...\n")
    if (len(l)>=3):
        print(red)
        print(f"El primer lugar con un tiempo de {l[0][1]}s es para {l[0][0]}")
        print(f"El segundo lugar con un tiempo de {l[1][1]}s es para {l[1][0]}")
        print(f"El tercer lugar con un tiempo de {l[2][1]}s es para {l[2][0]}")
        t.sleep(6)
    if (len(l)==2):
        print(green)
        print(f"El primer lugar con un tiempo de {l[0][1]}s es para {l[0][0]}")
        print(f"El segundo lugar con un tiempo de {l[1][1]}s es para {l[1][0]}")
        t.sleep(6)
    if (len(l)==1):
        print(yellow)
        t.sleep(6)
        print(f"El tiempo de {l[0][0]} fue de {l[0][1]}s")

def reporteNivel2(l:list):
    """Función que define el orden de los jugadores según su tiempo en 
    el nivel 2 por medio del método de ordenamiento por burbuja.

    Args:
        l (list): lista que llega por parámetro a la función. 
    """
    listaCopia2=l.copy()
    while True:
        cambio = False
        for e in range(len(listaCopia2)-1):
            if (listaCopia2[e][2]<listaCopia2[e+1][2]):
                pass
            else :
                temporal= listaCopia2[e]
                listaCopia2[e]=listaCopia2[e+1]
                listaCopia2[e+1]=temporal
                cambio=True
        if cambio == False:
            break
    imprimirReporte2(listaCopia2)

def imprimirReporte2(l:list):
    """Función encargada de imprimir en la terminal los resultados de los mejores
    tiempos de los jugadores en el nivel 1.

    Args:
        l (list): Lista que llega por parámetro a la función.
    """
    print (chr(27) + "[2J")
    print("Nivel dos completado...\n")
    if (len(l)>=3):
        print(red)
        print(f"El primer lugar con un tiempo de {l[0][2]}s es para {l[0][0]}")
        print(f"El segundo lugar con un tiempo de {l[1][2]}s es para {l[1][0]}")
        print(f"El tercer lugar con un tiempo de {l[2][2]}s es para {l[2][0]}")
        t.sleep(6)
    if (len(l)==2):
        print(green)
        print(f"El primer lugar con un tiempo de {l[0][2]}s es para {l[0][0]}")
        print(f"El segundo lugar con un tiempo de {l[1][2]}s es para {l[1][0]}")
        t.sleep(6)
    if (len(l)==1):
        print(yellow)
        t.sleep(6)
        print(f"El tiempo de {l[0][0]} fue de {l[0][2]}s")

def reporteNivel3(l:list):
    """Función que define el orden de los jugadores según su tiempo en 
    el nivel 3 por medio del método de ordenamiento por burbuja.

    Args:
        l (list): lista que llega por parámetro a la función. 
    """
    listaCopia3=l.copy()
    while True:
        cambio = False
        for e in range(len(listaCopia3)-1):
            if (listaCopia3[e][3]<listaCopia3[e+1][3]):
                pass
            else :
                temporal= listaCopia3[e]
                listaCopia3[e]=listaCopia3[e+1]
                listaCopia3[e+1]=temporal
                cambio=True
        if cambio == False:
            break
    imprimirReporte3(listaCopia3)

def imprimirReporte3(l:list):
    """Función encargada de imprimir en la terminal los resultados de los mejores
    tiempos de los jugadores en el nivel 1.

    Args:
        l (list): Lista que llega por parámetro a la función.
    """
    print (chr(27) + "[2J")
    print("Nivel tres completado...\n")
    if (len(l)>=3):
        print(red)
        print(f"El primer lugar con un tiempo de {l[0][3]}s es para {l[0][0]}")
        print(f"El segundo lugar con un tiempo de {l[1][3]}s es para {l[1][0]}")
        print(f"El tercer lugar con un tiempo de {l[2][3]}s es para {l[2][0]}")
        t.sleep(6)
    if (len(l)==2):
        print(green)
        print(f"El primer lugar con un tiempo de {l[0][3]}s es para {l[0][0]}")
        print(f"El segundo lugar con un tiempo de {l[1][3]}s es para {l[1][0]}")
        t.sleep(6)
    if (len(l)==1):
        print(yellow)
        print(f"El tiempo de {l[0][3]} fue de {l[0][0]}s")
        t.sleep(6)

def procesoJuego1(listaJugadores:list):
    """Función que ejecuta cada nivel sobre la lista de jugadores ingresados al juego por medio de la 
    importación de funciones dentro del archivo 'Niveles'. Además de llamar a las funciones encargargadas
    de imprimir los reportes de cada nivel y final del juego. Y se imprimen los créditos del juego.

    Args:
        listaJugadores (list): Lista de jugadores ingresados al sistema, siendo esta la original.
    """
    N.ejecucionPrimerNivel(listaJugadores)
    reporteNivel1(listaJugadores)
    N.ejecucionSegundoNivel(listaJugadores)
    reporteNivel2(listaJugadores)
    N.ejecucionTercerNivel(listaJugadores)
    reporteNivel3(listaJugadores)
    conteoFinal(listaJugadores)
    listaJugadores.clear()
    print("========")
    print("Creditos")
    print("========")
    print("Creadores\n Wilmer Azofeifa\nIgnacio Alpízar")
    print("¡¡¡Gracias por jugar nuestro Juego!!!")
    print("Gracias a los profesores por el material para el proyecto")
    t.sleep(30)
    menuJuego()

def menuJuego():
    """Función que hace papel del menu del juego, en este apartado, el usuario tiene acceso a generar nuevos jugadores
    poder empezar el juego. Además se validan los posibles errores quepueda presentar el código. 
    """
    while True:    
      print (chr(27) + "[2J")
      print (blue)
      print ("A) Para agregar un nuevo jugador")
      print ("B) Para empezar")
      print ("C) Salir del Juego")
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
      elif opcion.lower() == "c":
            break
      elif opcion.lower() != "a" and opcion.lower() != "b"  and opcion.lower() != "c":
         print (chr(27) + "[2J")
         print("Por favor ingrese una opción válida")
         t.sleep(2)

menuJuego()

