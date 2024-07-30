import random
from time import sleep
import turtle

def animacion(caracter,caracterEsc):
    x=-600
    y=-50
    if caracter!=0:
        for i in range(caracter):
            x+=50
    if caracterEsc != "n":
        mover.penup()
        mover.color("white")
        mover.goto(x,y)
        mover.begin_fill()
        mover.pendown()
        mover.goto(x,-y)
        mover.goto(x+50,-y)
        mover.goto(x+50,y)
        mover.goto(x,y)
        mover.end_fill()
        mover.color("black")
        mover.pendown()
        mover.goto(x,-y)
        mover.goto(x+50,-y)
        mover.goto(x+50,y)
        mover.goto(x,y)
        mover.penup()
        mover.goto(x+20,y+30)
        mover.write(caracterEsc,font=("courier",20, "bold"))
    #sleep(1)

doc=open("IDs.txt","w")
print("Menu del programa")
print("1. Manualmente")
print("2. Aleatoriamente")
cadena=""
animar=1#si se graficara
tam=0
eleccion=int(input("Eliga una opcion: "))
if eleccion==1: 
    cadena =input("Cadena: ")
    for i in cadena:
        tam+=1
        if tam>13:#no se animara muchos caracteres
            animar=0
            break
else:
    i=0
    cadena=cadena+"*"
    tam1=random.randint(1,25)
    while i!=tam1:
        cadena=cadena+"|"
        i+=1
    i=0
    cadena=cadena+"*"
    tam2=random.randint(1,25)
    while i!=tam2:
        cadena=cadena+"|"
        i+=1
    cadena=cadena+"*"
    tam=tam1+tam2
    if tam<10: animar=1# Si se animara
    else: animar=0#no se animara ya que hay mas de 10 caracteres

if animar==1:
    puntero=turtle.Turtle()
    puntero.pencolor("red")
    puntero.left(90)
    puntero.penup()
    #puntero.speed(1)
    xpunt=-575
    mover=turtle.Turtle()
    mover.hideturtle()
    mover.speed(0)
    est=turtle.Turtle()
    est.hideturtle()
    est.speed(0)
    est.penup()
    ventana = turtle.Screen()
    ventana.setup(1350,950)#definir dimension de ventanas
    x=-600
    y=-50
    cuadro=turtle.Turtle()
    cuadro.left(90)
    cuadro.speed(0)
    cuadro.penup()
    #cuadro.color("navy")
    for i in cadena:
        cuadro.goto(x,y)
        #cuadro.begin_fill()
        cuadro.pendown()
        cuadro.goto(x,-y)
        cuadro.goto(x+50,-y)
        cuadro.goto(x+50,y)
        cuadro.goto(x,y)
        #cuadro.end_fill()
        x=x+50
    x2=-580
    y2=-20
    z=0
    for i in cadena:
        cuadro.penup()
        cuadro.goto(x2,y2)
        cuadro.write(cadena[z],font=("courier",20, "bold"))
        z+=1
        x2=x2+50
    puntero.goto(xpunt,-50)

#Estados del automata
estado = 1
i=0
cadena2=""
while 1:
    try:
        cadena[i]#intenta acceder a la variable
    except:#si no puede es porque no hay mas caracteres
        cadena=cadena+"_"
    if estado==1:
        if cadena[i]=="*":#Pone un X se va a la derecha y estado 2
            doc.write(str(estado)+","+cadena+","+"R"+"\n")
            cadena2=cadena[:i]
            cadena2=cadena2+"X"
            cadena2=cadena2+cadena[i+1:]
            cadena=cadena2
            if animar==1: 
                est.clear()
                animacion(i,"X")
                xpunt+=50
                puntero.goto(xpunt,-50)
                est.goto(xpunt,-88)
                est.write(estado,font=("courier",20, "bold"))
            i+=1
            estado=2
    elif estado==2:
        if cadena[i]=="*":#Se va a la derecha y estado 3
            doc.write(str(estado)+","+cadena+","+"R"+"\n")
            if animar==1: 
                est.clear()
                est.goto(xpunt,-88)
                est.write(estado,font=("courier",20, "bold"))
                xpunt+=50
                animacion(i,"n")
                puntero.goto(xpunt,-50)
            i+=1
            estado=3
        elif cadena[i]=="|":#Se va a la derecha
            doc.write(str(estado)+","+cadena+","+"R"+"\n")
            if animar==1: 
                est.clear()
                est.goto(xpunt,-88)
                est.write(estado,font=("courier",20, "bold"))
                xpunt+=50
                animacion(i,"n")
                puntero.goto(xpunt,-50)
            i+=1
    elif estado==3:
        if cadena[i]=="*":#Pone un X se va a la izquierda y estado 4
            cadena2=cadena[:i]
            cadena2=cadena2+"X"
            cadena2=cadena2+cadena[i+1:]
            cadena=cadena2
            doc.write(str(estado)+","+cadena+","+"L"+"\n")
            if animar==1: 
                est.clear()
                est.goto(xpunt,-88)
                est.write(estado,font=("courier",20, "bold"))
                animacion(i,"X")
                xpunt-=50
                puntero.goto(xpunt,-50)
            i-=1
            estado=4
        elif cadena[i]=="|":#Se va a la derecha
            doc.write(str(estado)+","+cadena+","+"R"+"\n")
            if animar==1: 
                est.clear()
                est.goto(xpunt,-88)
                est.write(estado,font=("courier",20, "bold"))
                xpunt+=50
                animacion(i,"n")
                puntero.goto(xpunt,-50)
            i+=1  
    elif estado==4:
        if cadena[i]=="*":#Se va a la izquierda
            doc.write(str(estado)+","+cadena+","+"L"+"\n")
            if animar==1: 
                est.clear()
                est.goto(xpunt,-88)
                est.write(estado,font=("courier",20, "bold"))
                xpunt-=50
                animacion(i,"n")
                puntero.goto(xpunt,-50)
            i-=1
        elif cadena[i]=="|":#Pone una a, se va a la derecha y estado 5
            cadena2=cadena[:i]
            cadena2=cadena2+"a"
            cadena2=cadena2+cadena[i+1:]
            cadena=cadena2
            doc.write(str(estado)+","+cadena+","+"R"+"\n")
            if animar==1: 
                est.clear()
                est.goto(xpunt,-88)
                est.write(estado,font=("courier",20, "bold"))
                animacion(i,"a")
                xpunt+=50
                puntero.goto(xpunt,-50)
            i+=1 
            estado=5 
        elif cadena[i]=="X":#Se va a la derecha y estado 7
            doc.write(str(estado)+","+cadena+","+"R"+"\n")
            if animar==1:
                est.clear()
                est.goto(xpunt,-88)
                est.write(estado,font=("courier",20, "bold"))
                animacion(i,"n")  
                xpunt+=50
                puntero.goto(xpunt,-50)
            i+=1 
            estado=7
    elif estado==5:
        if cadena[i]=="_":#Pone un |, se va a la izquierda y estado 6
            cadena2=cadena[:i]
            cadena2=cadena2+"|"
            cadena2=cadena2+cadena[i+1:]
            cadena=cadena2
            doc.write(str(estado)+","+cadena+","+"L"+"\n")
            if animar==1: 
                est.clear()
                est.goto(xpunt,-88)
                est.write(estado,font=("courier",20, "bold"))
                animacion(i,"|")
                xpunt-=50
                puntero.goto(xpunt,-50)
            i-=1
            estado=6
        elif cadena[i]=="*":#Se va a la derecha
            doc.write(str(estado)+","+cadena+","+"R"+"\n")
            if animar==1:
                est.clear()
                est.goto(xpunt,-88)
                est.write(estado,font=("courier",20, "bold"))
                animacion(i,"n")
                xpunt+=50
                puntero.goto(xpunt,-50)

            i+=1
        elif cadena[i]=="|":#Se va a la derecha
            doc.write(str(estado)+","+cadena+","+"R"+"\n")
            if animar==1:
                est.clear()
                est.goto(xpunt,-88)
                est.write(estado,font=("courier",20, "bold"))
                animacion(i,"n") 
                xpunt+=50
                puntero.goto(xpunt,-50)
            i+=1
        elif cadena[i]=="X":#Se va a la derecha
            doc.write(str(estado)+","+cadena+","+"R"+"\n")
            if animar==1:
                est.clear()
                est.goto(xpunt,-88)
                est.write(estado,font=("courier",20, "bold"))
                animacion(i,"n") 
                xpunt+=50
                puntero.goto(xpunt,-50)
            i+=1
    elif estado==6:
        if cadena[i]=="*":#Se va a la izquierda
            doc.write(str(estado)+","+cadena+","+"L"+"\n")
            if animar==1:
                est.clear()
                est.goto(xpunt,-88)
                est.write(estado,font=("courier",20, "bold"))
                animacion(i,"n") 
                xpunt-=50
                puntero.goto(xpunt,-50)
            i-=1
        elif cadena[i]=="|":#Se va a la izquierda
            doc.write(str(estado)+","+cadena+","+"L"+"\n")
            if animar==1:
                est.clear()
                est.goto(xpunt,-88)
                est.write(estado,font=("courier",20, "bold"))
                animacion(i,"n") 
                xpunt-=50
                puntero.goto(xpunt,-50)
            i-=1
        elif cadena[i]=="a":#Pone un | se va a la izquierda y estado 4
            cadena2=cadena[:i]
            cadena2=cadena2+"|"
            cadena2=cadena2+cadena[i+1:]
            cadena=cadena2
            doc.write(str(estado)+","+cadena+","+"L"+"\n")
            if animar==1: 
                est.clear()
                est.goto(xpunt,-88)
                est.write(estado,font=("courier",20, "bold"))
                animacion(i,"|")
                xpunt-=50
                puntero.goto(xpunt,-50)
            i-=1
            estado=4
        elif cadena[i]=="X":#Se va a la izquierda
            doc.write(str(estado)+","+cadena+","+"L"+"\n")
            if animar==1:
                est.clear()
                est.goto(xpunt,-88)
                est.write(estado,font=("courier",20, "bold"))
                animacion(i,"n") 
                xpunt-=50
                puntero.goto(xpunt,-50)
            i-=1
    elif estado==7:
        if cadena[i]=="*":#Se va a la derecha y estado 8
            doc.write(str(estado)+","+cadena+","+"R"+"\n")
            if animar==1:
                est.clear()
                est.goto(xpunt,-88)
                est.write(estado,font=("courier",20, "bold"))
                animacion(i,"n") 
                xpunt+=50
                puntero.goto(xpunt,-50)
            i+=1
            estado=8
        elif cadena[i]=="|":#Se va a la derecha
            doc.write(str(estado)+","+cadena+","+"R"+"\n")
            if animar==1:
                est.clear()
                est.goto(xpunt,-88)
                est.write(estado,font=("courier",20, "bold"))
                animacion(i,"n") 
                xpunt+=50
                puntero.goto(xpunt,-50)
            i+=1
    elif estado==8:
        if cadena[i]=="_":#Pone un * se va a la izquierda y estado 9
            cadena2=cadena[:i]
            cadena2=cadena2+"*"
            cadena2=cadena2+cadena[i+1:]
            cadena=cadena2
            doc.write(str(estado)+","+cadena+","+"L"+"\n")
            if animar==1: 
                est.clear()
                est.goto(xpunt,-88)
                est.write(estado,font=("courier",20, "bold"))
                animacion(i,"*")
                xpunt-=50
                puntero.goto(xpunt,-50)
            i-=1
            estado=9
        elif cadena[i]=="|":#Se va a la derecha
            doc.write(str(estado)+","+cadena+","+"R"+"\n")
            if animar==1:
                est.clear()
                est.goto(xpunt,-88)
                est.write(estado,font=("courier",20, "bold"))
                animacion(i,"n") 
                xpunt+=50
                puntero.goto(xpunt,-50)
            i+=1
        elif cadena[i]=="X":#Pone un * y se va a la derecha
            cadena2=cadena[:i]
            cadena2=cadena2+"*"
            cadena2=cadena2+cadena[i+1:]
            cadena=cadena2
            doc.write(str(estado)+","+cadena+","+"R"+"\n")
            if animar==1: 
                est.clear()
                est.goto(xpunt,-88)
                est.write(estado,font=("courier",20, "bold"))
                animacion(i,"*")
                xpunt+=50
                puntero.goto(xpunt,-50)
            i+=1
    elif estado==9:
        if cadena[i]=="*":#Se va a la izquierda
            doc.write(str(estado)+","+cadena+","+"L"+"\n")
            if animar==1:
                est.clear()
                est.goto(xpunt,-88)
                est.write(estado,font=("courier",20, "bold"))
                animacion(i,"n") 
                xpunt-=50
                puntero.goto(xpunt,-50)
                
            i-=1
        elif cadena[i]=="|":#Se va a la izquierda
            doc.write(str(estado)+","+cadena+","+"L"+"\n")
            if animar==1:
                est.clear()
                est.goto(xpunt,-88)
                est.write(estado,font=("courier",20, "bold"))
                animacion(i,"n") 
                xpunt-=50
                puntero.goto(xpunt,-50)
            i-=1
        elif cadena[i]=="X":#Pone un * y !(se detiene el proceso)
            cadena2=cadena[:i]
            cadena2=cadena2+"*"
            cadena2=cadena2+cadena[i+1:]
            cadena=cadena2
            doc.write(str(estado)+","+cadena+","+"FIN"+"\n")
            if animar==1:
                est.clear()
                animacion(i,"*")
            break
sleep(3)
print("CadenaFinal: "+cadena)
doc.close()