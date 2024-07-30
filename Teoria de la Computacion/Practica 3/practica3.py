from random import randint #Libreria para generar numeros random
from time import sleep#libreria para que el programa espere
import os
import turtle#libreria para limpiar consola

def generadorCadenasBin(numCad,longitud):#Funcion para generar las cadenas binarias
    x=0
    a=open("CadenasGeneradas_{}.txt".format(n),"w")#Abrir archivo
    while(x!=numCad):#Numero de cadenas a generar
        y=0
        cadena=""#Declaramos la cadena y vaciamos para reutilizar la variable
        while(y!=longitud):#Longitud 64
            cadena=cadena+str(randint(0,1))#Juntar la cadena anterior para formar la nueva
            y+=1
        a.write(cadena+",") #Escribir en el archivo la cadena generada
        if(longitud==64): paridad(cadena) #Determinar si se grafica o se generar archivos
        else: graficoParidad(cadena)# Se genera el grafico
        x+=1
    a.close()

def paridad(cadena):
    estado=0
    i=0
    while i!=64:# Recorrer toda la cadena
        if(estado==0):# Estado incial y final
            d.write("f(q"+"0"+"-"+cadena[i]+")")# Imprimir en archivo en que estado se encuentra y que caracter recibe
            if cadena[i]=="1": estado=2# Cambio de estado
            else: estado=1 #Cambio de estado
            d.write("->q"+str(estado)+"||") # Escribir en documento hacia que estado se dirige
        elif(estado==1):
            d.write("f(q"+"1"+"-"+cadena[i]+")")
            if cadena[i]=="1": estado=3
            else: estado=0
            d.write("->q"+str(estado)+"||")
        elif(estado==2):
            d.write("f(q"+"2"+"-"+cadena[i]+")")
            if cadena[i]=="1": estado=0
            else: estado=3
            d.write("->q"+str(estado)+"||")
        elif(estado==3):
            d.write("f(q"+"2"+"-"+cadena[i]+")")
            if cadena[i]=="1": estado=1
            else: estado=2
            d.write("->q"+str(estado)+"||")
        i+=1
    d.write("\n")# Para diferenciar cada cadena 
    if(estado==0): b.write(cadena+",")# Se acepta la cadena y la escribe en el archivo
    else: c.write(cadena+",")# No acepta la cadena y la escribe en el archivo

def graficoParidad(cadena):
    tortuga.speed(9)#Aumentar velocidad de tortuga
    tortuga.penup#levantar tortuga
    tortuga.begin_fill()# donde empezara el relleno de la figura
    tortuga.color("black","cyan")# color de relleno
    tortuga.goto(-10,300)# Donde se dirige la tortuga
    tortuga.pendown()# bajar la tortuga
    tortuga.goto(-10,350)
    tortuga.goto(60,350)
    tortuga.goto(60,300)
    tortuga.goto(-10,300)
    tortuga.end_fill()# donde termin el relleno
    tortuga.goto(0,300)
    tortuga.write(cadena,font=9)# Escribir una cadena
    tortuga.penup()
    i=0
    tortuga.goto(-285,250)
    tortuga.pendown()
    tortuga.begin_fill()
    tortuga.goto(-285,270)
    tortuga.goto(-270,270)
    tortuga.goto(-270,250)
    tortuga.goto(-285,250)
    tortuga.end_fill()
    tortuga.goto(-280,250)
    tortuga.write(cadena[i],font=9)
    tortuga.penup()
    tortuga.speed(1)
    estado=0
    while(i!=6):
        if estado==0:#inicio q0 estado inicial
            if(cadena[i]=="1"):# si entra 1 entonces va a q2:
                tortuga.goto(-200,200)
                tortuga.pendown()
                tortuga.color("red")
                tortuga.goto(-200,-100)
                tortuga.color("black")
                tortuga.hideturtle()# ocultar tortuga para borrar linea roja
                tortuga.speed(9)
                tortuga.goto(-200,200)
                tortuga.showturtle()# enseñar la tortuga
                tortuga.goto(-200,-100)
                tortuga.speed(1)
                tortuga.penup()
                estado=2
            elif(cadena[i]=="0"):   #si entra 0 entonces va a q1:
                tortuga.goto(-150,250)
                tortuga.pendown()
                tortuga.color("red")
                tortuga.goto(150,250)
                tortuga.color("black")
                tortuga.hideturtle()
                tortuga.speed(10)
                tortuga.goto(-150,250)
                tortuga.showturtle()
                tortuga.goto(150,250)
                tortuga.speed(1)
                tortuga.penup()
                estado=1
        elif estado == 1: #q1 primer estado
            if(cadena[i]=="0"):    #entra 0 entonces va a q0
                tortuga.goto(150,250)
                tortuga.pendown()
                tortuga.color("red")
                tortuga.goto(-150,250)
                tortuga.color("black")
                tortuga.hideturtle()
                tortuga.speed(10)
                tortuga.goto(150,250)
                tortuga.showturtle()
                tortuga.goto(-150,250)
                tortuga.speed(1)
                tortuga.penup()
                estado=0
            if(cadena[i]=="1"):    #entra 1 entonces va a q3
                tortuga.goto(200,200)
                tortuga.pendown()
                tortuga.color("red")
                tortuga.goto(200,-100)
                tortuga.color("black")
                tortuga.hideturtle()
                tortuga.speed(10)
                tortuga.goto(200,200)
                tortuga.showturtle()
                tortuga.goto(200,-100)
                tortuga.speed(1)
                tortuga.penup()
                estado=3
        elif estado == 2:    #q2 Segundo estado
            if(cadena[i]=="0"):    #entra 0 entonces va a q3
                tortuga.goto(-150,-150)
                tortuga.pendown()
                tortuga.color("red")
                tortuga.goto(150,-150)
                tortuga.color("black")
                tortuga.hideturtle()
                tortuga.speed(10)
                tortuga.goto(-150,-150)
                tortuga.showturtle()
                tortuga.goto(150,-150)
                tortuga.speed(1)
                tortuga.penup()
                estado=3
            if(cadena[i]=="1"):    #entra 1 entonces va a q0
                tortuga.goto(-200,-100)
                tortuga.pendown()
                tortuga.color("red")
                tortuga.goto(-200,200)
                tortuga.color("black")
                tortuga.hideturtle()
                tortuga.speed(10)
                tortuga.goto(-200,-100)
                tortuga.showturtle()
                tortuga.goto(-200,200)
                tortuga.speed(1)
                tortuga.penup()
                estado=0
        elif estado == 3:     #q3 Tercer estado
            if(cadena[i]=="0"):    #entra 0 entonces va a q2
                tortuga.goto(150,-150)
                tortuga.pendown()
                tortuga.color("red")
                tortuga.goto(-150,-150)
                tortuga.color("black")
                tortuga.hideturtle()
                tortuga.speed(10)
                tortuga.goto(150,-150)
                tortuga.showturtle()
                tortuga.goto(-150,-150)
                tortuga.speed(1)
                tortuga.penup()
                estado=2
            if(cadena[i]=="1"):   #entra 1 entonces v a q1
                tortuga.goto(200,-100)
                tortuga.pendown()
                tortuga.color("red")
                tortuga.goto(200,200)
                tortuga.color("black")
                tortuga.hideturtle()
                tortuga.speed(9)
                tortuga.goto(200,-100)
                tortuga.showturtle()
                tortuga.goto(200,200)
                tortuga.speed(1)
                tortuga.penup()
                estado=1
        i+=1

rand=randint(0,1)
n=1
tortuga=turtle# declaracion de tortuga
while(rand!=0):
    rand=randint(0,1)# Determinar si el atuomata esta encendido o apagado
    if rand==1:# automata prendido
        print("El automata esta encendido")
        print("\tMenu del Automata")
        print("1. Continuar con el automata")
        print("2. Graficar AFD")
        opcion=input("Seleccione una opcion: ")
        if (opcion=="1"):# Generar las 10**6 cadenas longitud 64
            b=open("CadenasAceptadas_{}.txt".format(n),"w")# se abren los archivos
            c=open("CadenasRechazadas_{}.txt".format(n),"w")# Format para colocar el numero de archivo que corresponde
            d=open("Historia_{}.txt".format(n),"w")
            generadorCadenasBin(10**6,64)
            sleep(1)# El programa espera 1s
            b.close()#se cierran los archivos
            c.close()
            d.close()
        elif (opcion=="2"):# se genera l;a grafica
            tortuga.setup(900,800)# Se configura el recuadro 900px,800px
            tortuga.speed(9)
            tortuga.penup()
            tortuga.goto(-200,205)
            tortuga.pendown()
            tortuga.circle(45)# Se dibuja un circulo
            tortuga.penup()
            tortuga.goto(-200,200)#0
            tortuga.pendown()
            tortuga.circle(50)
            tortuga.penup()
            tortuga.goto(-205,240)
            tortuga.write("q0",font=9)# Se escriben dentro del circulo el estado que corresponde
            tortuga.goto(200,200)#1
            tortuga.pendown()
            tortuga.circle(50)
            tortuga.penup()
            tortuga.goto(195,240)
            tortuga.pendown()
            tortuga.write("q1",font=9)
            tortuga.penup()
            tortuga.goto(-200,-200)#2
            tortuga.pendown()
            tortuga.circle(50)
            tortuga.penup()
            tortuga.goto(-205,-155)
            tortuga.write("q2",font=9)
            tortuga.goto(200,-200)#3
            tortuga.pendown()
            tortuga.circle(50)
            tortuga.penup()
            tortuga.goto(195,-155)
            tortuga.write("q3",font=9)
            estado=0
            #1 izquierda
            tortuga.goto(-210,20)
            tortuga.pendown()
            tortuga.write("1",font=9)# Se escribe la opcion 1 o 0 que viene de la cadena
            tortuga.penup()
            #2 arriba
            tortuga.goto(0,250)
            tortuga.pendown()
            tortuga.write("0",font=9)
            tortuga.penup()
            #3 abajo
            tortuga.goto(0,-170)
            tortuga.pendown()
            tortuga.write("0",font=9)
            tortuga.penup()
            #4 derecha
            tortuga.goto(210,20)
            tortuga.pendown()
            tortuga.write("1",font=9)
            tortuga.penup()
            generadorCadenasBin(10,6)# se llama a la funcion que genera cadenas
            sleep(1)# se espera el programa 1s
            os.system("pause")# Se espera un enter para continuar
    else: 
        tortuga.bye()# Se despide a la tortuga
        break
    os.system("cls")# Se limpia la terminal
    n+=1# Se aumenta para el cambio de nombre de los archivos
print("El automata esta apagado")
