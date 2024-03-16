import time
import ARMem as ar
import random

white= "\033[0;36m"
red= "\033[0;31m"
yellow= "\033[1;33m"
black= "\033[0;30m"
green=  "\033[0;32m"
nocolor = "\033[0m"
blue    = "\033[0;34m"
morado  = "\033[0;35m"
cian    = "\033[0;36m"

def randomizarNivel1():
    """Función que escoge 3 números al azar de una lista definida, 
    eliminandolos posteriormente para evitar que se repitan, retornando 
    la lista con los números escogidos, la cual serán las iteraciones.
    """
    marcadores= [0,1,2,3,4]
    listaNivel1= []
    for x in range (3):
        num=random.choice(marcadores)       #random.choice: Funcion importada que escoge un elemento al azar de una lista.
        marcadores.remove(num)
        listaNivel1.append(num)
    return(listaNivel1)

def randomizarNivel2():
    """Función que escoge 4 números al azar de una lista definida, 
    eliminandolos posteriormente para evitar que se repitan, retornando 
    la lista con los números escogidos, la cual serán las iteraciones.
    """
    marcadores= [0,1,2,3,4]
    listaNivel2= []
    for x in range (4):
        num=random.choice(marcadores)       #random.choice: Funcion importada que escoge un elemento al azar de una lista.
        marcadores.remove(num)
        listaNivel2.append(num)
    return(listaNivel2)

def randomizarNivel3():
    """Función que escoge 5 números al azar de una lista definida, 
    eliminandolos posteriormente para evitar que se repitan, retornando 
    la lista con los números escogidos, la cual seran las iteraciones.
    """
    marcadores= [0,1,2,3,4]
    listaNivel3= []
    for x in range (5):
        num=random.choice(marcadores)       #random.choice: Funcion importada que escoge un elemento al azar de una lista.
        marcadores.remove(num)
        listaNivel3.append(num)
    return(listaNivel3)

def cicloNivel1():
    """Función que concatena las listas retornadas por la función 
    randomizarNivel1 para obtener las 5 iteraciones del nivel 1.
    """
    listaNivel1= []
    for i in range(5):
        ciclos=randomizarNivel1()
        listaNivel1.append(ciclos)
    return(listaNivel1)

def cicloNivel2():
    """Función que concatena las listas retornadas por la funcion 
    randomizarNivel2 para obtener las 5 iteraciones del nivel 2.
    """
    listaNivel2= []
    for i in range(5):
        ciclos=randomizarNivel2()
        listaNivel2.append(ciclos)
    return(listaNivel2)

def cicloNivel3():
    """Función que concatena las listas retornadas por la funcion 
    randomizarNivel3 para obtener las 5 iteraciones del nivel 3.
    """
    listaNivel3= []
    for i in range(5):
        ciclos=randomizarNivel3()
        listaNivel3.append(ciclos)
    return(listaNivel3)

def primerNivel():
    """Función que con ayuda del código proporcionado para la realizacion
    del proyecto define en que consiste el nivel 1, haciendo también un cambio
    en la impresión para que muestre al usuario la lista con el nombre de las 
    frutas y no la lista de numeros de cada marcador.
    """
    listaJuego1= cicloNivel1()
    print('\033[2J')  # Código ANSI para limpiar la pantalla en sistemas Windows
    tiempoTotal=0
    for x in listaJuego1:
        print(blue)
        print(f'Memorice la siguiente secuencia...')
        print("\n")
        listaFrutas= []
        for i in x:
            if(i==0):
                listaFrutas.append("Piña")
            if(i==1):
                listaFrutas.append("Cereza")
            if(i==2):
                listaFrutas.append("Uva")
            if(i==3):
                listaFrutas.append("Pera")
            if(i==4):
                listaFrutas.append("Guanabana")
        print(listaFrutas)
        print("\n")
        time.sleep(5)
        print(f'Ordene los marcadores en el orden que se le indicó!')
        time.sleep(3)
        print('\033[2J')  # Código ANSI para limpiar la pantalla en sistemas Windows
        tiempoPartida=round(ar.start_sorting(x,flip_image=True,show_images=True, show_coordinates=False, show_ids=False, show_identified_marker=False)  ,2)
        tiempoTotal+=tiempoPartida
        tiempoTotal=round(tiempoTotal,2)
        print(f'Tiempo de partida: {tiempoPartida}s')
        time.sleep(7)
        print('\033[2J')  # Código ANSI para limpiar la pantalla en sistemas Windows
    print()
    print (f'El usuario ha completado el primer nivel en un tiempo de {tiempoTotal}s')
    time.sleep(2)
    return(tiempoTotal)

def segundoNivel():
    """Función que con ayuda del código proporcionado para la realizacion
    del proyecto define en que consiste el nivel 2, haciendo también un cambio
    en la impresión para que muestre al usuario la lista con el nombre de las 
    frutas y no la lista de números de cada marcador.
    """
    listaJuego2= cicloNivel2()
    print('\033[2J')  # Código ANSI para limpiar la pantalla en sistemas Windows
    tiempoTotal=0
    for x in listaJuego2:
        print(f'Memorice la siguiente secuencia...')
        print("\n")
        #print(x)
        listaFrutas= []
        for i in x:
            if(i==0):
                listaFrutas.append("Piña")
            if(i==1):
                listaFrutas.append("Cereza")
            if(i==2):
                listaFrutas.append("Uva")
            if(i==3):
                listaFrutas.append("Pera")
            if(i==4):
                listaFrutas.append("Guanabana")
        print(listaFrutas)
        print("\n")
        time.sleep(6)
        print(f'Ordene los marcadores en el orden que se le indicó!')
        time.sleep(4) 
        print('\033[2J')  # Código ANSI para limpiar la pantalla en sistemas Windows
        tiempoPartida=round(ar.start_sorting(x,flip_image=True,show_images=True, show_coordinates=False, show_ids=False, show_identified_marker=False)  ,2)
        tiempoTotal+=tiempoPartida
        tiempoTotal=round(tiempoTotal,2)
        print('\033[2J')    # Código ANSI para limpiar la pantalla en sistemas Windows
        print(f'Tiempo de partida: {tiempoPartida}s')
        time.sleep(7)  
        print('\033[2J')  # Código ANSI para limpiar la pantalla en sistemas Windows
    print (f'El usuario ha completado el segundo nivel en un tiempo de {tiempoTotal}s')
    time.sleep(2)
    return(tiempoTotal)

def tercerNivel():
    """Funcion que con ayuda del codigo proporcionado para la realizacion
    del proyecto define en que consiste el nivel 3, haciendo tambien un cambio
    en la impresion para que muestre al usuario la lista con el nombre de las 
    frutas y no la lista de numeros de cada marcador.
    """
    listaJuego3=cicloNivel3()
    print('\033[2J')  # Código ANSI para limpiar la pantalla en sistemas Windows
    tiempoTotal=0
    for x in listaJuego3:
        print(f'Memorice la siguiente secuencia...')
        print("\n")
        #print(x)
        listaFrutas= []
        for i in x:
            if(i==0):
                listaFrutas.append("Piña")
            if(i==1):
                listaFrutas.append("Cereza")
            if(i==2):
                listaFrutas.append("Uva")
            if(i==3):
                listaFrutas.append("Pera")
            if(i==4):
                listaFrutas.append("Guanabana")
        print(listaFrutas)
        print("\n")
        time.sleep(7)
        print(f'Ordene los marcadores en el orden que se le indicó!')
        time.sleep(4)
        print('\033[2J')  # Código ANSI para limpiar la pantalla en sistemas Windows
        tiempoPartida=round(ar.start_sorting(x,flip_image=True,show_images=True, show_coordinates=False, show_ids=False, show_identified_marker=False)  ,2)
        tiempoTotal+=tiempoPartida
        tiempoTotal=round(tiempoTotal,2)
        print(f'Tiempo de partida: {tiempoPartida}s')
        time.sleep(7)
        print('\033[2J')  # Código ANSI para limpiar la pantalla en sistemas Windows
    print (f'El usuario ha completado el tercer nivel en un tiempo de {tiempoTotal}s')
    time.sleep(2)
    return(tiempoTotal)

def ejecucionPrimerNivel(li:list):
    """Función que llamando a la funcioón primerNivel ejecuta el nivel 1 para cada 
    jugador que se ingrese en la lista de jugadores mediante el menu.

    Args:
        li (list): Lista de jugadores ingresada mediante el menu.
    """
    print('\033[2J')    # Código ANSI para limpiar la pantalla en sistemas Windows
    print(green)
    print("Comenzando nivel 1...")
    time.sleep(3)
    contador= 0
    for jugador in li:
        time.sleep(2)
        print(white)
        print("Turno de", li[contador][0])
        time.sleep(2)
        tiempoJugador=primerNivel()
        lis= li[contador]
        lis.insert(1,tiempoJugador)
        contador+=1
        time.sleep(2)

def ejecucionSegundoNivel(li:list):
    """Función que llamando a la función segundoNivel ejecuta el nivel 2 para cada 
    jugador que se ingrese en la lista de jugadores mediante el menu.

    Args:
        li (list): Lista de jugadores ingresada mediante el menu.
    """
    print('\033[2J')    # Código ANSI para limpiar la pantalla en sistemas Windows
    print(yellow)
    print("Comenzando nivel 2...")
    time.sleep(3)
    contador= 0
    for jugador in li:
        time.sleep(2)
        print(white)
        print("Turno de", li[contador][0])
        time.sleep(2)
        tiempoJugador=segundoNivel()
        lis= li[contador]
        lis.insert(2,tiempoJugador)
        contador+=1
        time.sleep(2)

def ejecucionTercerNivel(li:list):
    """Función que llamando a la función tercerNivel ejecuta el nivel 3 para cada 
    jugador que se ingrese en la lista de jugadores mediante el menu.

    Args:
        li (list): Lista de jugadores ingresada mediante el menu.
    """
    print('\033[2J')    # Código ANSI para limpiar la pantalla en sistemas Windows
    print(red)
    print("Comenzando nivel 3...")
    time.sleep(3)
    contador= 0
    for jugador in li:
        time.sleep(2)
        print(white)
        print("Turno de", li[contador][0])
        time.sleep(2)
        tiempoJugador=tercerNivel()
        lis= li[contador]
        lis.insert(3,tiempoJugador)
        contador+=1
        time.sleep(2)
