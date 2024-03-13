import ARMem as ar
import time

def primerNivel():
    listaJuego=[[0,1,2],[4,3,0],[4,3,1],[0,4,3],[2,0,1]]


    print('\033[2J')  # Código ANSI para limpiar la pantalla en sistemas Windows
    tiempoTotal=0
    for x in listaJuego:
        print(f'Memorice la siguiente secuencia...')
        print(x)
        time.sleep(5)
        print(f'Ordene los marcadores en el orden que se le indicó!')
        time.sleep(3)

        print('\033[2J')  # Código ANSI para limpiar la pantalla en sistemas Windows
        tiempoPartida=round(ar.start_sorting(x,flip_image=True,show_images=True, show_coordinates=False, show_ids=False, show_identified_marker=False)  ,2)
        tiempoTotal+=tiempoPartida
        print(f'Tiempo de partida: {tiempoPartida}s')

        time.sleep(7)
        print('\033[2J')  # Código ANSI para limpiar la pantalla en sistemas Windows

    print (f'El usuario ha completado el juego en un tiempo de {tiempoTotal}s')
    segundoNivel()


def segundoNivel():
    listaJuego=[[0,1,2,4],[4,3,2,1],[4,2,1,0],[2,1,4,3],[3,2,0,1]]
    
    
    print('\033[2J')  # Código ANSI para limpiar la pantalla en sistemas Windows
    tiempoTotal=0
    for x in listaJuego:
        print(f'Memorice la siguiente secuencia...')
        print(x)
        time.sleep(5)
        print(f'Ordene los marcadores en el orden que se le indicó!')
        time.sleep(3)
        
        print('\033[2J')  # Código ANSI para limpiar la pantalla en sistemas Windows
    
        tiempoPartida=round(ar.start_sorting(x,flip_image=True,show_images=True, show_coordinates=False, show_ids=False, show_identified_marker=False)  ,2)
        tiempoTotal+=tiempoPartida
        print(f'Tiempo de partida: {tiempoPartida}s')
    
        time.sleep(7)
        print('\033[2J')  # Código ANSI para limpiar la pantalla en sistemas Windows
    
    print (f'El usuario ha completado el juego en un tiempo de {tiempoTotal}s')
    tercerNivel()



def tercerNivel():
    listaJuego=[[0,1,2,3,4],[4,3,2,1,0],[4,3,2,1,0],[0,2,1,4,3],[3,4,2,0,1]]
    
    
    print('\033[2J')  # Código ANSI para limpiar la pantalla en sistemas Windows
    tiempoTotal=0
    for x in listaJuego:
        print(f'Memorice la siguiente secuencia...')
        print(x)
        time.sleep(5)
        print(f'Ordene los marcadores en el orden que se le indicó!')
        time.sleep(3)
        
        print('\033[2J')  # Código ANSI para limpiar la pantalla en sistemas Windows
    
        tiempoPartida=round(ar.start_sorting(x,flip_image=True,show_images=True, show_coordinates=False, show_ids=False, show_identified_marker=False)  ,2)
        tiempoTotal+=tiempoPartida
        print(f'Tiempo de partida: {tiempoPartida}s')
    
        time.sleep(7)
        print('\033[2J')  # Código ANSI para limpiar la pantalla en sistemas Windows
    
    print (f'El usuario ha completado el juego en un tiempo de {tiempoTotal}s')

    