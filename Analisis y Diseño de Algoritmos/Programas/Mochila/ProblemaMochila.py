import numpy as np
import os
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

class objeto():
    def __init__(self):
        self.nombre=input("Nombre: ")
        self.peso=int(input("Peso: "))
        self.ganancia=int(input("Ganancia: "))
    def __str__(self):
        cadena="Nombre:   "+self.nombre+"\n"+"Peso:     "+str(self.peso)+" Kg"+"\n"+"Ganancia: "+str(self.ganancia)+" Kg"
        return cadena
    
class casilla():
    def __init__(self):
        self.entro='N'
        self.coordenada='(0,0)'
        self.ganancia=0
    def __str__(self):
        cadena=self.entro+" "+self.coordenada+" "+str(self.ganancia)
        return cadena

def principal():
    clearConsole()
    j=False
    while j==False:
        try:
            cantidadObjetos=int(input("Cantidad de objetos a disponibles: "))
            Capacidad=int(input("Capacidad de la mochila: "))
            Capacidad+=1
            j=True
            clearConsole()
        except:
            print("Introduce un numero valido")
            j=False
            clearConsole()
    objetos=[]
    i=0
    j=1
    while i!=cantidadObjetos:
        print("Objeto #"+str(j))
        objetos.append(objeto())
        clearConsole()
        i+=1
        j+=1
    cantidadObjetos+=1
    listaCasillas = np.zeros(shape=(cantidadObjetos,Capacidad), dtype=casilla)
    i=0
    while i!=cantidadObjetos:
        j=0
        while j!=Capacidad:
            listaCasillas[i][j]=casilla()
            j+=1
        i+=1
    i=1
    print("Introdujiste los siguientes datos:")
    print("Capacidad de la mochila: "+str(Capacidad-1)+" Kg"+"\n")
    for x in objetos:
        print("Objeto #"+str(i))
        i+=1
        print(str(x)+"\n"+"----------------------------------")
    os.system("Pause")
    clearConsole()
    ren=[]
    maximizar(Capacidad,cantidadObjetos,listaCasillas,Capacidad,objetos,1,1,0,ren)
    i=0
    while i!=cantidadObjetos:
        j=0
        print("")
        while j!=Capacidad:
            print(str(listaCasillas[i][j])+" ",end=" ") 
            j+=1
        i+=1
    print('\n'+"Los objetos para la resoluccion de problema son:")#obtencion de la solucion final, se
    x=0
    while x!=len(ren):
        c=int(ren[x])-1
        print(objetos[c].nombre+' , ',end='')
        x+=1


def maximizar(columna,renglon,lista,capacidad,objeto,c,r,o,ren):#condiciones evaluadas
    if objeto[o].peso>c:
        lista[r][c].entro="N"
        lista[r][c].coordenada="("+str(r-1)+","+str(c)+")"
        lista[r][c].ganancia=lista[r-1][c].ganancia

    elif c>=objeto[o].peso:#aplicacion de reglas
        lista[r][c].entro="S"
        nose=lista[r-1][c].ganancia
        y=c-objeto[o].peso
        nose2=lista[r-1][y].ganancia+objeto[o].ganancia
        lista[r][c].coordenada="("+str(r-1)+","+str(y)+")"
        if nose>nose2:
            lista[r][c].ganancia=nose
        else:
            lista[r][c].ganancia=nose2
    if c==columna-1:
        if r==renglon-1:
            x=1
            while c!=0 or r!=0:#Seleccion de optimos
                lista[r][c].entro='\033[92m'+lista[r][c].entro
                lista[r][c].ganancia=str(lista[r][c].ganancia)+'\033[0m'
                r1=r
                r=int(lista[r][c].coordenada[1])
                c=int(lista[r1][c].coordenada[3])
                if x==1:
                    ren.append(r1) 
                if lista[r][c].entro=="S":
                    ren.append(r)
                    x=0    
            return 1
        c=1
        r+=1
        o+=1
        maximizar(columna,renglon,lista,capacidad,objeto,c,r,o,ren)
    else:    
        c+=1 
        maximizar(columna,renglon,lista,capacidad,objeto,c,r,o,ren)

principal()