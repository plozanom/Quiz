from simple_term_menu import TerminalMenu
from random import randint
import time
import os

from rich.panel import Panel
from rich.console import Console
from rich.text import Text
from rich.progress import track

import general as gn
import geografia as geo
import historia as his
import literatura as lit
import musica as mus
from puntuacion import Puntuacion, Tabla

reglas ='''
[bold yellow]-[/] Se le hara una pregunta con cuatro posibles respuestas.
[bold yellow]-[/] Cada pregunta bien respondida le hará acreedor a [bold cyan]U$50[/].
[bold yellow]-[/] Al haber tenido una respuesta correcta, aparecera un menu
  preguntando si desea continuar, si la respuesta es si
  se seguira a la siguiente pregunta, [bold cyan]si la respuesta es no
  usted se retira del juego y es premiado con el monto 
  que lleve acumulado[/].
[bold yellow]-[/] Si falla alguna pregunta, usted será sacado del juego y [bold cyan]no
  podra quedarse con el monto que lleve acumulado[/].
[bold yellow]-[/] Si decide retirarse o termina el juego, su nombre sera
  registrado junto con el numero de preguntas que logro
  responder. Esta informacion se podra ver en la seccion de [bold cyan]puntuaciones.
'''

class Menu:

    def __init__(self,contador=0,preguntas_correctas=0):
        self.n = randint(1,7)
        self.contador = contador
        self.correctas = preguntas_correctas

        self.console = Console()

    def principal(self):#Menu Principal
        #Despligue del menu
        titulo = '\nBienvenidos a un juego de preguntas y respuestas\n¿Que desea hacer?\n'
        main = ['Ver las Reglas','Ir al Juego','Puntuaciones', 'Salir']
        main_menu = TerminalMenu(main, title=titulo,menu_cursor_style=('fg_green','bold'), menu_cursor='>> ')

        
        self.console.print(Panel(Text('Quiz Game',style='cyan', justify='center'),border_style='cyan'))#Titulo del juego
        opciones = main_menu.show()
        eleccion = main[opciones]

        #Funcionalidades de las opciones
        if eleccion == 'Ver las Reglas':
            self.console.print(Panel(reglas, title='[bold]Reglas', border_style='yellow'))
            volver = ['Volver al Menu Principal']
            volver_menu=TerminalMenu(volver,menu_cursor_style=('fg_green','bold'), menu_cursor='>> ')
            
            opciones = volver_menu.show()
            eleccion = volver[opciones]
            if eleccion == 'Volver al Menu Principal':
                os.system('clear')
                Menu.principal(self)
        elif eleccion == 'Puntuaciones':
            os.system('clear')
            Tabla().dibujar_tabla()
            volver = ['Volver al Menu Principal']
            volver_menu=TerminalMenu(volver,menu_cursor_style=('fg_green','bold'), menu_cursor='>> ')
            
            opciones = volver_menu.show()
            eleccion = volver[opciones]
            if eleccion == 'Volver al Menu Principal':
                os.system('clear')
                Menu.principal(self)
        elif eleccion == 'Salir':
            os.system('clear')
            quit()
    
    def bool_menu(self):#Submenu para elegir si seguir jugando o terminar el juego
        booleano = ['Si','No']
        boolmenu = TerminalMenu(booleano, title='¿Desea continuar?', clear_screen=True, menu_cursor_style=('fg_green','bold'), menu_cursor='>> ')

        opciones = boolmenu.show()
        eleccion = booleano[opciones]

        if eleccion == 'Si':
            print('\n\n\n\n')
            for i in track(range(5), description='\tPreparando la siguiente pregunta...'):
                time.sleep(0.25)
        else:
            nombre = str(self.console.input('[bold cyan]Has decidido retirate\nPor havor escribe tu nombre >>> '))
            p = Puntuacion(nombre,self.correctas,self.contador)
            p.actualizar_csv()
            self.console.print(f'Respondiste {self.correctas} pregunta correcta\nHas ganado U${self.contador}')
            quit()
        
    def pregunta1(self):#Primera pregunta
        respuestas = gn.posibles_respuestas[self.n-1]
        menu = TerminalMenu(respuestas, title=gn.preguntas[self.n-1], clear_screen=True,menu_cursor_style=('fg_green','bold'), menu_cursor='>> ')
        
        self.console.print(Panel('Pregunta #1'))
        opciones = menu.show()
        eleccion = respuestas[opciones]

        if eleccion == gn.respuesta_correcta[self.n-1]:
            self.contador+=50
            self.correctas+=1
            self.console.print(f'\n\n\n\n\t\t[green]Genial!!![/]\n\tTienes {self.correctas} pregunta correcta\n\tLlevas acumulado U${self.contador}\n\n\n\n')
            time.sleep(1)
        else:
            self.console.print(f'\n\n\n\n\t\t[red]Incorrecto!!![/]\n\tRespondiste {self.correctas} preguntas correctas\n\n\n\n')
            quit()
        
    def pregunta2(self):#Segunda pregunta
        respuestas = geo.posibles_respuestas[self.n-1]
        menu = TerminalMenu(respuestas, title=geo.preguntas[self.n-1], clear_screen=True,menu_cursor_style=('fg_green','bold'), menu_cursor='>> ')
        
        opciones = menu.show()
        eleccion = respuestas[opciones]

        if eleccion == geo.respuesta_correcta[self.n-1]:
            self.contador+=50
            self.correctas+=1
            self.console.print(f'\n\n\n\n\t\t[green]Genial!!![/]\n\tTienes {self.correctas} pregunta correcta\n\tLlevas acumulado U${self.contador}\n\n\n\n')
            time.sleep(1)
        else:
            self.console.print(f'\n\n\n\n\t\t[red]Incorrecto!!![/]\n\tRespondiste {self.correctas} pregunta correcta\n\n\n\n')
            quit()
    
    def pregunta3(self):#Tercera pregunta
        respuestas = his.posibles_respuestas[self.n-1]
        menu = TerminalMenu(respuestas, title=his.preguntas[self.n-1], clear_screen=True,menu_cursor_style=('fg_green','bold'), menu_cursor='>> ')
        
        opciones = menu.show()
        eleccion = respuestas[opciones]

        if eleccion == his.respuesta_correcta[self.n-1]:
            self.contador+=50
            self.correctas+=1
            self.console.print(f'\n\n\n\n\t\t[green]Genial!!![/]\n\tTienes {self.correctas} pregunta correcta\n\tLlevas acumulado U${self.contador}\n\n\n\n')
            time.sleep(1)
        else:
            self.console.print(f'\n\n\n\n\t\t[red]Incorrecto!!![/]\n\tRespondiste {self.correctas} preguntas correctas\n\n\n\n')
            quit()
    
    def pregunta4(self):#Cuarta pregunta
        respuestas = mus.posibles_respuestas[self.n-1]
        menu = TerminalMenu(respuestas, title=mus.preguntas[self.n-1], clear_screen=True,menu_cursor_style=('fg_green','bold'), menu_cursor='>> ')

        opciones = menu.show()
        eleccion = respuestas[opciones]

        if eleccion == mus.respuesta_correcta[self.n-1]:
            self.contador+=50
            self.correctas+=1
            self.console.print(f'\n\n\n\n\t\t[green]Genial!!![/]\n\tTienes {self.correctas} pregunta correcta\n\tLlevas acumulado U${self.contador}\n\n\n\n')
            time.sleep(1)
        else:
            self.console.print(f'\n\n\n\n\t\t[red]Incorrecto!!![/]\n\tRespondiste {self.correctas} preguntas correctas\n\n\n\n')
            quit()
    
    def pregunta5(self):#Quinta pregunta
        respuestas = lit.posibles_respuestas[self.n-1]
        menu = TerminalMenu(respuestas, title=lit.preguntas[self.n-1], clear_screen=True,menu_cursor_style=('fg_green','bold'), menu_cursor='>> ')

        opciones = menu.show()
        eleccion = respuestas[opciones]

        if eleccion == lit.respuesta_correcta[self.n-1]:
            self.contador+=50
            self.correctas+=1
        else:
            self.console.print(f'\n\n\n\n\t\t[red]Incorrecto!!![/]\n\tRespondiste {self.correctas} preguntas correctas\n\n\n\n')
            quit()
    
    def volver_menu(self):#Menu para elegir si volver al menu principal o salir del juego
        volver = ['Si','No']
        volver_menu=TerminalMenu(volver,title='¿Desea volver al Menu Principal?', menu_cursor_style=('fg_green','bold'), menu_cursor='>> ')
            
        opciones = volver_menu.show()
        eleccion = volver[opciones]
        if eleccion == 'Si':
            os.system('clear')
            Menu.principal(self)
        else:
            os.system('clear')
            quit()