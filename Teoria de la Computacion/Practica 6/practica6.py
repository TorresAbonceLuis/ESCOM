import random
import sys, os
from time import sleep
import turtle
def animacion(ES,numeroX):
    if numeroX==0:
        if ES==1:#Entra una X
            X10.goto(0,170)
            X10.shape(rutaX1)
            X10.goto(0,-315)
    elif numeroX==1:
        if ES==1:#Entra una X
            X9.goto(0,170)
            X9.shape(rutaX2)
            X9.goto(0,-265)
        else:#Sale una X
            X10.goto(0,170)
            X10.hideturtle()
    elif numeroX==2:
        if ES==1:
            X8.goto(0,170)
            X8.shape(rutaX2)
            X8.goto(0,-215)
        else:
            X9.goto(0,170)
            X9.hideturtle()
    elif numeroX==3:
        if ES==1:
            X7.goto(0,170)
            X7.shape(rutaX2)
            X7.goto(0,-165)
        else:
            X8.goto(0,170)
            X8.hideturtle()
    elif numeroX==4:
        if ES==1:
            X6.goto(0,170)
            X6.shape(rutaX2)
            X6.goto(0,-115)
        else:
            X7.goto(0,170)
            X7.hideturtle()
    elif numeroX==5:
        if ES==1:
            X5.goto(0,170)
            X5.shape(rutaX2)
            X5.goto(0,-65)
        else:
            X6.goto(0,170)
            X6.hideturtle()
    if numeroX==6:
        if ES==1:
            X4.goto(0,170)
            X4.shape(rutaX2)
            X4.goto(0,-15)
        else:
            X5.goto(0,170)
            X5.hideturtle()
    elif numeroX==7:
        if ES==1:#Entra una X
            X3.goto(0,170)
            X3.shape(rutaX2)
            X3.goto(0,35)
        else:#Sale una X
            X4.goto(0,170)
            X4.hideturtle()
    elif numeroX==8:
        if ES==1:
            X2.goto(0,170)
            X2.shape(rutaX2)
            X2.goto(0,85)
        else:
            X3.goto(0,170)
            X3.hideturtle()
    elif numeroX==9:
        if ES==1:
            X1.goto(0,170)
            X1.shape(rutaX2)
            X1.goto(0,135)
        else:
            X2.goto(0,170)
            X2.hideturtle()
    elif numeroX==10:
            X1.goto(0,170)
            X1.hideturtle()

doc=open("ids.txt","w")#abrir archivo
print("Menu:")
print("Ingresar cadena.")
print("1. Manual.")
print("2. Aleatoriamente")
eleccion=int(input("Elige una opcion: "))
w=0
if eleccion==1: 
    cadena=input("Introduce la cadena: ")
    for i in cadena:
        w=w+1#tamanio de la cadena
else: 
    cadena=''
    x=random.randint(1,100)#Longitud 1-100,000
    y=0
    while(y!=x):
        cadena=cadena+"0"#Juntar la cadena anterior para formar la nueva
        y+=1
    z=random.randint(1,100)
    y=0
    while(y!=z):
        cadena=cadena+"1"#Juntar la cadena anterior para formar la nueva
        y+=1
    w=x+z
if w>10: animar=1 #comprbar animacion
else: animar=0
def rutaImagen(nombreImagen):#recibe 1 argumento
    pathScript=sys.argv[0]#ruta de este codigo
    carpeta,script=os.path.split(pathScript)#ruta de la carpeta 
    pathFondo=os.path.join(carpeta, nombreImagen)#Obtiene la ruta absoluta
    return pathFondo#regresa la ruta
#iniciamos la animacion
if animar==0:
    ventana = turtle.Screen()
    ventana.setup(1350,950)#definir dimension de ventanas
    rutaX1=rutaImagen("X.gif")
    rutaX2=rutaImagen("X.gif")
    rutaX3=rutaImagen("X.gif")
    rutaX4=rutaImagen("X.gif")
    rutaX5=rutaImagen("X.gif")
    rutaX6=rutaImagen("X.gif")
    rutaX7=rutaImagen("X.gif")
    rutaX8=rutaImagen("X.gif")
    rutaX9=rutaImagen("X.gif")
    rutaX10=rutaImagen("X.gif")
    ventana.addshape(rutaX1)
    ventana.addshape(rutaX2)
    ventana.addshape(rutaX3)
    ventana.addshape(rutaX4)
    ventana.addshape(rutaX5)
    ventana.addshape(rutaX6)
    ventana.addshape(rutaX7)
    ventana.addshape(rutaX8)
    ventana.addshape(rutaX9)
    ventana.addshape(rutaX10)
    X1=turtle.Turtle()
    X2=turtle.Turtle()
    X3=turtle.Turtle()
    X4=turtle.Turtle()
    X5=turtle.Turtle()
    X6=turtle.Turtle()
    X7=turtle.Turtle()
    X8=turtle.Turtle()
    X9=turtle.Turtle()
    X10=turtle.Turtle()
    X1.speed(1)
    X1.penup()
    X2.speed(1)
    X2.penup()
    X3.speed(1)
    X3.penup()
    X4.speed(1)
    X4.penup()
    X5.speed(1)
    X5.penup()
    X6.speed(1)
    X6.penup()
    X7.speed(1)
    X7.penup()
    X8.speed(1)
    X8.penup()
    X9.speed(1)
    X9.penup()
    X10.speed(1)
    X10.penup()
    tortuCuad=turtle.Turtle()
    tortuCuad.speed(0)
    tortuCuad.penup()
    tortuCuad.color("navy")
    tortuCuad.begin_fill()
    tortuCuad.goto(-150,-340)
    tortuCuad.goto(150,-340)
    tortuCuad.goto(150,150)
    tortuCuad.goto(-150,150)
    tortuCuad.goto(-150,-340)
    tortuCuad.end_fill()
    tortuCuad.goto(-500,0)
    tortuCuad.write("Cadena:"+cadena,font=("courier",20, "bold"))
    tortuCuad.left(90)
    p=-381
    tortuCuad.goto(p,0)
pila=[]#declaramos la pila
y=0
i=0
exis=0
alfa="Z0"
doc.write("q"+","+cadena+","+alfa+"\n")
while(y!=w):
    if animar==0: p+=16
    if cadena[y] == "0":#estado q
        pila.append("x")#agregar X
        alfa="X"+alfa
        doc.write("q"+","+cadena[y:]+","+alfa+"\n")
        if animar==0:#la cadena es menor a 10 entonces se grafica
            animacion(1,exis)
            tortuCuad.goto(p,0)
            exis+=1
    elif cadena[y] == "1":#estado p
        try:
            pila.pop()#Quitar X
            doc.write("p"+","+cadena[y:]+","+alfa[i:]+"\n")
            if animar==0:
                animacion(0,exis)
                tortuCuad.goto(p,0)
                exis-=1
            i+=1
        except:
            doc.write("f"+","+cadena[y-1:]+","+alfa[i-1:]+"\n")
            if animar==0:
                tortuCuad.goto(200,0)
                tortuCuad.write("Cadena no Aceptada \nhay mas 1s que 0s",font=("courier",20, "bold"))
                sleep(5)
            doc.close()
            exit(1)
    y+=1
if not pila:#estado f
    print("Ta vacia")#estado f aceptado
    doc.write("f"+","+"vacio"+","+alfa[i:]+"\n")
    if animar==0:
        tortuCuad.goto(200,0)
        tortuCuad.write("Cadena Aceptada hay \n0s y 1s por igual",font=("courier",20, "bold"))
        sleep(5)
else:
    doc.write("f"+","+cadena[y-1:]+","+alfa[i-1:]+"\n")
    if animar==0:
        tortuCuad.goto(200,0)
        tortuCuad.write("Cadena no Aceptada hay \nmas 0s que 1s",font=("courier",20, "bold"))
        sleep(5)
doc.close()