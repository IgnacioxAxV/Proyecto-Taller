import time
import ARMem as ar
import random

white= "\033[0;36m"
red= "\033[0;31m"
yellow= "\033[1;33m"
black= "\033[0;30m"
green=  "\033[0;32m"

def randomizarNivel1():
    markers= [0,1,2,3,4]
    listaNivel1= []
    for x in range (3):
        num=random.choice(markers)
        markers.remove(num)
        listaNivel1.append(num)
    return(listaNivel1)

def randomizarNivel2():
    markers= [0,1,2,3,4]
    listaNivel2= []
    for x in range (4):
        num=random.choice(markers)
        markers.remove(num)
        listaNivel2.append(num)
    return(listaNivel2)

def randomizarNivel3():
    markers= [0,1,2,3,4]
    listaNivel3= []
    for x in range (5):
        num=random.choice(markers)
        markers.remove(num)
        listaNivel3.append(num)
    return(listaNivel3)

def cicloNivel1():
    lis= []
    for i in range(5):
        ciclos=randomizarNivel1()
        lis.append(ciclos)
    return(lis)

def cicloNivel2():
    lis= []
    for i in range(5):
        ciclos=randomizarNivel2()
        lis.append(ciclos)
    return(lis)

def cicloNivel3():
    lis= []
    for i in range(5):
        ciclos=randomizarNivel3()
        lis.append(ciclos)
    return(lis)

def primerNivel():
    listaJuego=[[0,1,2],[4,3,0],[4,3,1],[0,4,3],[2,0,1]]
    listaJuego= cicloNivel1()



    print('\033[2J')  # Código ANSI para limpiar la pantalla en sistemas Windows
    tiempoTotal=0
    for x in listaJuego:
        print(f'Memorice la siguiente secuencia...')
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

    print (f'El usuario ha completado el primer nivel en un tiempo de {tiempoTotal}s')
    return(tiempoTotal)


def segundoNivel():
    listaJuego=[[0,1,2,4],[4,3,2,1],[4,2,1,0],[2,1,4,3],[3,2,0,1]]
    listaJuego= cicloNivel2()
    
    print('\033[2J')  # Código ANSI para limpiar la pantalla en sistemas Windows
    tiempoTotal=0
    for x in listaJuego:
        print(f'Memorice la siguiente secuencia...')
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
        time.sleep(5)
        print(f'Ordene los marcadores en el orden que se le indicó!')
        time.sleep(3)
        
        print('\033[2J')  # Código ANSI para limpiar la pantalla en sistemas Windows
    
        tiempoPartida=round(ar.start_sorting(x,flip_image=True,show_images=True, show_coordinates=False, show_ids=False, show_identified_marker=False)  ,2)
        tiempoTotal+=tiempoPartida
        #tiempoTotal=round(tiempoTotal,2)
        print('\033[2J')    # Código ANSI para limpiar la pantalla en sistemas Windows
        print(f'Tiempo de partida: {tiempoPartida}s')
    
        time.sleep(7)     
        print('\033[2J')  # Código ANSI para limpiar la pantalla en sistemas Windows
    
    print (f'El usuario ha completado el segundo nvel en un tiempo de {tiempoTotal}s')
    return(tiempoTotal)


def tercerNivel():
    listaJuego=[[0,1,2,3,4],[4,3,2,1,0],[4,3,2,1,0],[0,2,1,4,3],[3,4,2,0,1]]
    
    
    print('\033[2J')  # Código ANSI para limpiar la pantalla en sistemas Windows
    tiempoTotal=0
    for x in listaJuego:
        print(f'Memorice la siguiente secuencia...')
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
        time.sleep(5)
        print(f'Ordene los marcadores en el orden que se le indicó!')
        time.sleep(3)
        
        print('\033[2J')  # Código ANSI para limpiar la pantalla en sistemas Windows
    
        tiempoPartida=round(ar.start_sorting(x,flip_image=True,show_images=True, show_coordinates=False, show_ids=False, show_identified_marker=False)  ,2)
        tiempoTotal+=tiempoPartida
        print(f'Tiempo de partida: {tiempoPartida}s')
    
        time.sleep(7)
        print('\033[2J')  # Código ANSI para limpiar la pantalla en sistemas Windows
    
    print (f'El usuario ha completado el tercer nivel en un tiempo de {tiempoTotal}s')
    return(tiempoTotal)

jugadores=[["Juan"],["Pablo"]]
def ejecucionPrimerNivel(li:list):
    print('\033[2J')    # Código ANSI para limpiar la pantalla en sistemas Windows
    print(red)
    print("Comenzando nivel 1...")
    time.sleep(3)
    co= 0
    for jugador in li:
        time.sleep(2)

        print(white)
        print("Turno de", li[co][0])
        time.sleep(2)
        
        tjugador=primerNivel()
        lis= li[co]
        lis.insert(1,tjugador)
        co+=1

def ejecucionSegundoNivel(li:list):
    print('\033[2J')    # Código ANSI para limpiar la pantalla en sistemas Windows
    print(red)
    print("Comenzando nivel 2...")
    time.sleep(3)
    co= 0
    for jugador in li:
        time.sleep(2)

        print(white)
        print("Turno de", li[co][0])
        time.sleep(2)
        
        tjugador=segundoNivel()
        lis= li[co]
        lis.insert(2,tjugador)
        co+=1

def ejecucionTercerNivel(li:list):
    print('\033[2J')    # Código ANSI para limpiar la pantalla en sistemas Windows
    print(red)
    print("Comenzando nivel 3...")
    time.sleep(3)
    co= 0
    for jugador in li:
        time.sleep(2)

        print(white)
        print("Turno de", li[co][0])
        time.sleep(2)
        
        tjugador=tercerNivel()
        lis= li[co]
        lis.insert(3,tjugador)
        co+=1

ejecucionPrimerNivel(jugadores)
ejecucionSegundoNivel(jugadores)
ejecucionTercerNivel(jugadores)

print(jugadores)