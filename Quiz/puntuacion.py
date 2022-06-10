#Modulo para la creacion, actualizacion y visualizacion de las puntuaciones
import csv
import pathlib

from rich.console import Console
from rich.table import Table
from rich import box

class Puntuacion:

    def __init__(self, nombre, correctas, total):
        self.nombre = nombre
        self.correctas =  correctas
        self.total = total
        self.archivo = 'puntuacion.csv'
        
    def actualizar_csv(self):
        encabezados = ['Nombre','R. correctas','Total']

        if not pathlib.Path(self.archivo).exists():
            with open(self.archivo, 'w', newline='') as f:
                writer = csv.writer(f, fieldnames=encabezados)
                writer.writeheader()

        with open(self.archivo, 'a', newline='') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerow([self.nombre,self.correctas,self.total])
        
class Tabla:
    def __init__(self) -> None:
        self.archivo = 'puntuacion.csv'
    
    def organizar_datos(self):
        datos = []
        with open(self.archivo, 'r') as f:
            lineas = f.read().splitlines()
            for linea in lineas:
                l = linea.split(',')
                datos.append([l[0],l[1],l[2]])

        datos.sort(key= lambda dato:dato[1], reverse=True)

        return datos
    
    def dibujar_tabla(self):
        datos = Tabla().organizar_datos()

        table = Table(title='Ranking de Puntuaciones', border_style='yellow',box=box.DOUBLE_EDGE)
        console = Console()

        table.add_column('Nombre')
        table.add_column('Respuesta Correctas', justify='right', no_wrap=True)
        table.add_column('Total', justify='right')

        datos.pop(0)

        for dato in datos:
            table.add_row(dato[0],dato[1],dato[2])
        
        console.print(table)