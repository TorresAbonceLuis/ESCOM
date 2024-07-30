from tkinter import CENTER
import turtle
import sys, os
import random
import time

#Definimos la ruta de las pieza
def generarRuta(cadena,estado,camino,ficha):
    if(estado==0):#si el estado actual es ese entra a la condicion
        camino=camino+"00"#Se escribe el camnio que va llevando
        if len(cadena)== 1 or 0:
            if ficha ==0:#Dependiendo de la ficha escribe en el documento
                caminosO.write(camino+",")
            else:
                caminosX.write(camino+",")
            return#retornar a la ultima funcion
        else:
            cadena=cadena[1:]
            if(cadena[0]=="b"):#2 opciones mover a blancas
                generarRuta(cadena,1,camino,ficha)#mover al estado
                generarRuta(cadena,4,camino,ficha)
            else: generarRuta(cadena,5,camino,ficha)#1 opcion mover a negras
    elif(estado==1):
        camino=camino+"01"
        if len(cadena)==1:
            if ficha ==0:
                caminosO.write(camino+",")
            else:
                caminosX.write(camino+",")
            return
        else:
            cadena=cadena[1:]
            if(cadena=="b"):
                generarRuta(cadena,4,camino,ficha)
                generarRuta(cadena,6,camino,ficha)
            else:
                generarRuta(cadena,0,camino,ficha)
                generarRuta(cadena,5,camino,ficha)
                generarRuta(cadena,2,camino,ficha)
    elif(estado==2):
        camino=camino+"02"
        if len(cadena)==1:
            if ficha ==0:
                caminosO.write(camino+",")
            else:
                caminosX.write(camino+",")
            return
        else:
            cadena=cadena[1:]
            if(cadena=="b"):
                generarRuta(cadena,1,camino,ficha)
                generarRuta(cadena,6,camino,ficha)
                generarRuta(cadena,3,camino,ficha)
            else:
                generarRuta(cadena,5,camino,ficha)
                generarRuta(cadena,7,camino,ficha)
    elif(estado==3):
        camino=camino+"03"
        if len(cadena)==1:
            if ficha ==0:
                caminosO.write(camino+",")
            else:
                caminosX.write(camino+",")
            return
        else:
            cadena=cadena[1:]
            if(cadena=="b"): generarRuta(cadena,6,camino,ficha)
            else:
                generarRuta(cadena,7,camino,ficha)
                generarRuta(cadena,2,camino,ficha)
    elif(estado==4):
        camino=camino+"04"
        if len(cadena)==1:
            if ficha ==0:
                caminosO.write(camino+",")
            else:
                caminosX.write(camino+",")
            return
        else:
            cadena=cadena[1:]
            if(cadena=="b"):
                generarRuta(cadena,1,camino,ficha)
                generarRuta(cadena,9,camino,ficha)
            else:
                generarRuta(cadena,0,camino,ficha)
                generarRuta(cadena,5,camino,ficha)
                generarRuta(cadena,8,camino,ficha)
    elif(estado==5):
        camino=camino+"05"
        if len(cadena)==1:
            if ficha ==0:
                caminosO.write(camino+",")
            else:
                caminosX.write(camino+",")
            return
        else:
            cadena=cadena[1:]
            if(cadena=="b"):
                generarRuta(cadena,1,camino,ficha)
                generarRuta(cadena,4,camino,ficha)
                generarRuta(cadena,6,camino,ficha)
                generarRuta(cadena,9,camino,ficha)
            else:
                generarRuta(cadena,0,camino,ficha)
                generarRuta(cadena,8,camino,ficha)
                generarRuta(cadena,2,camino,ficha)
                generarRuta(cadena,10,camino,ficha)
    elif(estado==6):
        camino=camino+"06"
        if len(cadena)==1:
            if ficha ==0:
                caminosO.write(camino+",")
            else:
                caminosX.write(camino+",")
            return
        else:
            cadena=cadena[1:]
            if(cadena=="b"):
                generarRuta(cadena,1,camino,ficha)
                generarRuta(cadena,3,camino,ficha)
                generarRuta(cadena,9,camino,ficha)
                generarRuta(cadena,11,camino,ficha)
            else:
                generarRuta(cadena,2,camino,ficha)
                generarRuta(cadena,5,camino,ficha)
                generarRuta(cadena,7,camino,ficha)
                generarRuta(cadena,10,camino,ficha)
    elif(estado==7):
        camino=camino+"07"
        if len(cadena)==1:
            if ficha ==0:
                caminosO.write(camino+",")
            else:
                caminosX.write(camino+",")
            return
        else:
            cadena=cadena[1:]
            if(cadena=="b"):
                generarRuta(cadena,3,camino,ficha)
                generarRuta(cadena,6,camino,ficha)
                generarRuta(cadena,11,camino,ficha)
            else:
                generarRuta(cadena,2,camino,ficha)
                generarRuta(cadena,10,camino,ficha)
                
    elif(estado==8):
        camino=camino+"08"
        if len(cadena)==1:
            if ficha ==0:
                caminosO.write(camino+",")
            else:
                caminosX.write(camino+",")
            return
        else:
            cadena=cadena[1:]
            if(cadena=="b"):
                generarRuta(cadena,4,camino,ficha)
                generarRuta(cadena,9,camino,ficha)
                generarRuta(cadena,12,camino,ficha)
            else:
                generarRuta(cadena,5,camino,ficha)
                generarRuta(cadena,13,camino,ficha)
    elif(estado==9):
        camino=camino+"09"
        if len(cadena)==1:
            if ficha ==0:
                caminosO.write(camino+",")
            else:
                caminosX.write(camino+",")
            return
        else:
            cadena=cadena[1:]
            if(cadena=="b"):
                generarRuta(cadena,4,camino,ficha)
                generarRuta(cadena,6,camino,ficha)
                generarRuta(cadena,12,camino,ficha)
                generarRuta(cadena,14,camino,ficha)
            else:
                generarRuta(cadena,5,camino,ficha)
                generarRuta(cadena,8,camino,ficha)
                generarRuta(cadena,13,camino,ficha)
                generarRuta(cadena,10,camino,ficha)
    elif(estado==10):
        camino=camino+"10"
        if len(cadena)==1:
            if ficha ==0:
                caminosO.write(camino+",")
            else:
                caminosX.write(camino+",")
            return
        else:
            cadena=cadena[1:]
            if(cadena=="b"):
                generarRuta(cadena,6,camino,ficha)
                generarRuta(cadena,9,camino,ficha)
                generarRuta(cadena,14,camino,ficha)
                generarRuta(cadena,11,camino,ficha)
            else:
                generarRuta(cadena,5,camino,ficha)
                generarRuta(cadena,7,camino,ficha)
                generarRuta(cadena,15,camino,ficha)
                generarRuta(cadena,13,camino,ficha)
    elif(estado==11):
        camino=camino+"11"
        if len(cadena)==1:
            if ficha ==0:
                caminosO.write(camino+",")
            else:
                caminosX.write(camino+",")
            return
        else:
            cadena=cadena[1:]
            if(cadena=="b"):
                generarRuta(cadena,6,camino,ficha)
                generarRuta(cadena,14,camino,ficha)
            else:
                generarRuta(cadena,7,camino,ficha)
                generarRuta(cadena,10,camino,ficha)
                generarRuta(cadena,15,camino,ficha)
    elif(estado==12):
        camino=camino+"12"
        if len(cadena)==1:
            if ficha ==0:
                caminosO.write(camino+",")
            elif ficha==1:
                caminosX.write(camino+",")
                listaX.append(camino)#Si llega a este punto es el camino gandor
                ganadorX.write(camino+",")#de esa ficha
            return
        else:
            cadena=cadena[1:]
            if(cadena=="b"): generarRuta(cadena,9,camino,ficha)
            else:
                generarRuta(cadena,8,camino,ficha)
                generarRuta(cadena,13,camino,ficha)
    elif(estado==13):
        camino=camino+"13"
        if len(cadena)==1:
            if ficha ==0:
                caminosO.write(camino+",")
            return
        else:
            cadena=cadena[1:]
            if(cadena=="b"):
                generarRuta(cadena,12,camino,ficha)
                generarRuta(cadena,9,camino,ficha)
                generarRuta(cadena,14,camino,ficha)
            else:
                generarRuta(cadena,8,camino,ficha)
                generarRuta(cadena,10,camino,ficha)
    elif(estado==14):
        camino=camino+"14"
        if len(cadena)==1:
            if ficha ==0:
                caminosO.write(camino+",")
            else:
                caminosX.write(camino+",")
            return
        else:
            cadena=cadena[1:]
            if(cadena=="b"):
                generarRuta(cadena,9,camino,ficha)
                generarRuta(cadena,11,camino,ficha)
            else:
                generarRuta(cadena,13,camino,ficha)
                generarRuta(cadena,10,camino,ficha)
                generarRuta(cadena,15,camino,ficha)
    elif(estado==15):
        camino=camino+"15"
        if len(cadena)==1:
            if ficha ==0:
                caminosO.write(camino+",")
                listaO.append(camino)#Si llega a este punto es el camino gandor
                ganadorO.write(camino+",")#de esta ficha
            else:
                caminosX.write(camino+",")
            return
        else:
            cadena=cadena[1:]
            if(cadena=="b"):
                generarRuta(cadena,14,camino,ficha)
                generarRuta(cadena,11,camino,ficha)
            else: generarRuta(cadena,10,camino,ficha)
#Recalcular ruta
def recalcularRuta(camino,estado,posicion,ficha,estado2):
    camino=camino[:posicion]
    listaX.clear()
    listaO.clear()
    if ficha==0:
        generarRuta(cadena1[int(posicion/2):],int(estado),"",0)
        random.shuffle(listaO)#elegir uno alazar
        for i in listaO:
            if i[2:4]!=estado2:#Elegir un estado diferente al que la otra ficha es igual
                camino=camino+i#Escribir el camino recalculado
                return camino
    else:
        generarRuta(cadena2[int(posicion/2):],int(estado),"",1)
        random.shuffle(listaX)
        for i in listaX:
            if i[2:4]!=estado2:
                camino=camino+i
                return camino
    return 1#se debe saltar turno

#Obtener la ruta absoluta de la imagen
def rutaImagen(nombreImagen):#recibe 1 argumento
    pathScript=sys.argv[0]
    carpeta,script=os.path.split(pathScript)
    pathFondo=os.path.join(carpeta, nombreImagen)#Obtiene la ruta absoluta
    return pathFondo#regresa la ruta
def moverXO(XO,estado):
    XO.speed(1)
    if(estado=="00"):
        XO.goto(-240,240)
        estado=0
    elif(estado=="01"):
        XO.goto(-80,240)
        estado=1
    elif(estado=="02"):
        XO.goto(80,240)
        estado=2
    elif(estado=="03"):
        XO.goto(240,240)
        estado=3
    elif(estado=="04"):
        XO.goto(-240,80)
        estado=4
    elif(estado=="05"):
        XO.goto(-80,80)
        estado=5
    elif(estado=="06"):
        XO.goto(80,80)
        estado=6
    elif(estado=="07"):
        XO.goto(240,80)
        estado=7
    elif(estado=="08"):
        XO.goto(-240,-80)
        estado=8
    elif(estado=="09"):
        XO.goto(-80,-80)
        estado=9
    elif(estado=="10"):
        XO.goto(80,-80)
        estado=10
    elif(estado=="11"):
        XO.goto(240,-80)
        estado=11
    elif(estado=="12"):
        XO.goto(-240,-240)
        estado=12
    elif(estado=="13"):
        XO.goto(-80,-240)
        estado=13
    elif(estado=="14"):
        XO.goto(80,-240)
        estado=14
    elif(estado=="15"):
        XO.goto(240,-240)
        estado=15
    return estado
#Menu del programa
print("Menu del programa:")
print("1. Automatico todo")
print("2. Manual")
opcion= int(input("Elige una opcion: "))
#Variables
caminosO=open("CaminosO.txt","w")
caminosX=open("caminosX.txt","w")
ganadorO=open("ganadorO.txt","w")
ganadorX=open("ganadorX.txt","w")
listaO=[]
listaX=[]
cadena1=""
cadena2=""
i=0
if (opcion==1):#damos valor aleatorio a la cadena
    numPiezas=2
    #numPiezas=random.randint(1,2)#con cuantas piezas jugara
    print("Num piezas: "+str(numPiezas))
    while (1):
        rango=random.randint(1,10)
        if numPiezas==2:
            while i != rango:
                cadena1=cadena1+random.choice(["b","n"])#generar cadena aleatoria
                cadena2=cadena2+random.choice(["b","n"])#generar cadena aleatoria
                i+=1
            try:#inteta generar rutas
                generarRuta(cadena1,0,"",0)
                generarRuta(cadena2,3,"",1)
                a=listaO[0]
                b=listaX[0]
                break
            except:#si da un error vaciamos las listas 
                listaX=[]
                listaO=[]
                cadena1=''#borramos contenido de los strings
                cadena2=''
                i=0
        else:
            while i != rango:
                cadena1=cadena1+random.choice(["b","n"])#generar cadena aleatoria
                i+=1
            try:
                generarRuta(cadena1,0,"",0)
                a=listaO[0]
                break
            except:
                listaO=[]
                cadena1=''
                i=0
else: 
    numPiezas=int(input("Piezas a jugar (1 o 2): "))#num de piezas a jugar
    aleat=input("generar aleatoriamente las cadenas s/n:")
    if aleat=="s":
        while(1):
            rango=random.randint(1,10)#establecer rango
            while i != rango:
                cadena1=cadena1+random.choice(["b","n"])
                if numPiezas==2: cadena2=cadena2+random.choice(["b","n"])
                i+=1
            try:
                generarRuta(cadena1,0,"",0)
                a=listaO[0]
                if numPiezas==2: 
                    generarRuta(cadena2,3,"",1)
                    b=listaX[0]
                break
            except:
                listaO=[]
                cadena1=''
                if numPiezas==2:
                    listaX=[]
                    cadena2=''
                i=0
    else:
        print("(solo caracteres: 'b' y 'n' sin espacio)") 
        cadena1=input("Primera cadena: ")
        generarRuta(cadena1,0,"",0)
        if os.stat('ganadorO.txt').st_size == 0:
            print("no se puede ganar listas de ganadores vacias")
            exit()
        if numPiezas==2: 
            cadena2=input("Segunda Cadena: ")
            generarRuta(cadena2,3,"",1)
            if os.stat('ganadorX.txt').st_size == 0:
                print("no se puede ganar listas de ganadores vacias")
#Obtenemos las rutas de las imagenes
rutaO=rutaImagen("O.gif")
rutaX=rutaImagen("X.gif")
tablero=rutaImagen("tablero.gif")
ganadorImg=rutaImagen("ganador.gif")
#Creamos la ventana
ventana = turtle.Screen()#Crear la ventana
ventana.setup(1350,950)#Dar dimensiones a ventana
ventana.bgpic(tablero)#Poner imagen de fondo
ventana.addshape(rutaO)#Insertar imagenes
ventana.addshape(rutaX)
ventana.addshape(ganadorImg)
#circulo en lugar de inicio
O=turtle.Turtle()
O.penup()
O.speed(0)
O.goto(-240,240)
O.speed(1)
estadoO=0 #iniciar estado de O
O.shape(rutaO)#Muestra la imagen
if numPiezas==2:#cruz en lugar de inicio
    X=turtle.Turtle()
    X.penup()
    X.speed(0)
    X.goto(240,240)
    X.speed(1)
    estadoX=3#inciar estado de X
    X.shape(rutaX)
#inicializamos variables
tortucad=turtle#tortuga para actualizar cadenas
tortucad.speed(0)
if numPiezas==2:#Asignar turno
    if random.randint(0,1)==1: turnoActivo="O"#asignar primer turno
    else: turnoActivo="X"#asignar primer turno
    tortucad.penup()
    tortucad.goto(-650,220)
    tortucad.write("Empieza:"+turnoActivo,font=("courier",20, "bold"))
#crear cuadro del costado
tortucad.hideturtle()
tortucad.penup()
tortucad.goto(-650,200)
tortucad.pendown()
tortucad.goto(-350,200)
tortucad.goto(-350,115)
tortucad.goto(-650,115)
tortucad.goto(-650,200)
tortucad.penup()
#crear cuadro de abajo
g=-650#no se cambia
h=100
k=-350#no se cambia
n=55
l=-645#no se cambia
y1=70
y2=50
def reinciarCuadro(cad1,cad2,g,h,k,n,l,y1,y2):
    tortucad=turtle
    tortucad.color("cyan")
    tortucad.speed(0)
    tortucad.hideturtle()
    tortucad.penup()
    tortucad.goto(g,h)
    tortucad.begin_fill()
    tortucad.pendown()
    tortucad.goto(k,h)
    tortucad.goto(k,n)
    tortucad.goto(g,n)
    tortucad.goto(g,h)
    tortucad.end_fill()
    tortucad.color("black")
    tortucad.penup()
    tortucad.goto(l,y1)
    tortucad.write("O:"+cad1,font=("courier",15, "bold"))
    tortucad.goto(l,y2)
    tortucad.write("X:"+cad2,font=("courier",15, "bold"))   
tortucad.penup()
tortucad.goto(-645,165)
tortucad.write("Cadenas de las fichas",font=("courier",15,"bold"))
tortucad.goto(-645,140)
tortucad.write("O:"+cadena1,font=("courier",15, "bold"))
if numPiezas==2:
    tortucad.goto(-645,115)
    tortucad.write("X:"+cadena2,font=("courier",15, "bold"))
#Elegir ganadores:
ganO=random.choice(listaO)
if numPiezas==2: ganX=random.choice(listaX)
#Mover piezas:
j=0
i=0
ganador=""
tortustado=turtle
if numPiezas==2:
    reinciarCuadro(ganO,ganX,g,h,k,n,l,y1,y2)
    x=0
    while(1):
        try:
            ganO[i]#comprobar que no esta vacio
            ganX[j]
        except:
            break#Termino y se rompe el ciclo
        if turnoActivo=="O":
            x=0
            if ganO[i:i+2]==ganX[j:j+2]:#comprobar si se encuentran en el mismo lugar
                a=recalcularRuta(ganX,ganX[j-2:j],j-2,1,ganX[j:j+2])#recalcular ruta
                if a == 1:
                    print("saltar turno")
                    x=1
                else:
                    ganX=a
                    h=h-45
                    n=n-45
                    y1=y1-45
                    y2=y2-45
                    reinciarCuadro(ganO,ganX,g,h,k,n,l,y1,y2)
                    x=0
            if moverXO(O,ganO[i:i+2])==15:
                ganador=0
                break
            time.sleep(.5)
            if x==0:
                if ganO[i+2:i+4]==ganX[j:j+2]:
                    a=recalcularRuta(ganX,ganX[j-2:j],j-2,1,ganX[j:j+2])
                    if a == 1:
                        print("saltar turno")
                        x=1
                    else:
                        ganX=a
                        h=h-45
                        n=n-45
                        y1=y1-45
                        y2=y2-45
                        reinciarCuadro(ganO,ganX,g,h,k,n,l,y1,y2)
                        x=0
                if x!=1:
                    if moverXO(X,ganX[i:i+2])==12:
                        ganador=1
                        break
                    time.sleep(.5)
                    j+=2
            i+=2
        else:
            x=0
            if ganO[i:i+2]==ganX[j:j+2]:
                a=recalcularRuta(ganO,ganO[i-2:i],i-2,0,ganO[i:i+2])
                if a == 1:
                    print("saltar turno")
                    x=1
                else:
                    ganO=a
                    h=h-45
                    n=n-45
                    y1=y1-45
                    y2=y2-45
                    reinciarCuadro(ganO,ganX,g,h,k,n,l,y1,y2)
                    x=0
            if moverXO(X,ganX[j:j+2])==12:
                ganador=1
                break
            time.sleep(.5)
            if x==0:
                if ganO[i:i+2]==ganX[j+2:j+4]:
                    a=recalcularRuta(ganO,ganO[i-2:j],i-2,0,ganO[i:i+2])
                    if a == 1:
                        print("saltar turno")
                        x=1
                    else:
                        ganO=a
                        h=h-45
                        n=n-45
                        y1=y1-45
                        y2=y2-45
                        reinciarCuadro(ganO,ganX,g,h,k,n,l,y1,y2)
                        x=0
                if x!=1:
                    if moverXO(O,ganO[i:i+2])==15:
                        ganador=0
                        break
                    i+=2
                    time.sleep(.5)
            j+=2
else:
    tortustado.goto(-645,70)
    tortustado.write("O:"+ganO,font=("courier",15, "bold"))
    for i in ganO:
        moverXO(O,ganO[j:j+2])
        j+=2
#cerrar documentos
caminosX.close()
caminosO.close()
ganadorO.close()
ganadorX.close()

ventana.clear()#limpiamos imagen
ventana.bgpic(ganadorImg)#definimos otro fondo
tortudor=turtle#generamos otra tortuga
tortudor.hideturtle()#ocultamos tortuga
    
if ganador==1:
    tortudor.speed(0)
    tortudor.color("black")
    tortudor.write("El ganador es X",font=("courier",40, "bold"),align=CENTER)#escribimos el ganador
else:
    tortudor.speed(0)
    tortudor.color("black")
    tortudor.write("El ganador es O",font=("courier",40, "bold"),align=CENTER)

ventana.mainloop()#La ventana corra todo el programa