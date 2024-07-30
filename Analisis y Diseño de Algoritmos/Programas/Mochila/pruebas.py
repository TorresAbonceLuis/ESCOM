"""
class objeto():
    def __init__(self):
        self.nombre=input("Entro: ")
        self.peso=input("coordenada: ")
        self.ganancia=int(input("Ganancia: "))
    def __str__(self):
        cadena=self.nombre+str(self.peso)+str(self.ganancia)
        return cadena

a=objeto()
import numpy as np
renglones = 5
columnas = 7
matriz0 = np.zeros(shape=(renglones,columnas), dtype=object)
print(matriz0)
matriz0[0][0]=str(a)
import numpy
x = numpy.array([[85, 86, 87, 88, 89], 
                 [90, 191, 192, 93, 94], 
                 [95, 96, 97, 98, 99], 
                 [100,101,102,103,104]])

row_labels = ['Z', 'Y', 'X', 'W']
column_labels = ['A', 'B', 'C', 'D', 'E']
import pandas
df = pandas.DataFrame(x, columns=column_labels, index=row_labels)
df"""