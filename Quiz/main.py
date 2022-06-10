from rich.console import Console

import os

import menu as mt
from puntuacion import Puntuacion

def main():
    while True:
        
        menu = mt.Menu()
        os.system('clear')

        #principal
        menu.principal()
        #1
        menu.pregunta1()
        
        #------
        
        menu.bool_menu()
        
        #2
        menu.pregunta2()
        
        #------
        menu.bool_menu()
        
        #3
        menu.pregunta3()
        
        #------
        menu.bool_menu()
        
        #4
        menu.pregunta4()
        
        #------
        menu.bool_menu()
        
        #5
        menu.pregunta5()
        
        #Fin
        nombre = str(Console().input('[bold cyan]Escribe tu nombre >>> '))
        p = Puntuacion(nombre,menu.correctas,menu.contador)
        p.actualizar_csv()
        Console().print(f'\n\n\n\n\t\t[green]Felicidades {nombre}!!!\n\tLlegaste hasta el final!!, Has ganado [bold cyan]U${menu.contador}[/]\n\n\n\n')
        
        #Volver a empezar
        menu.volver_menu()

if __name__ == '__main__':
    main()