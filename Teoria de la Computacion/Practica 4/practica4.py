from time import sleep
import turtle
print("1. Ver automata\n2. Correr Automata")
menu=int(input("Elige una opcion: "))
if menu == 1:
    tortu=turtle
    tortu.speed(0)
    tortu.setup(1350,950)
    tortu.penup()
    tortu.goto(-620,0)#A
    tortu.pendown()
    tortu.circle(40)
    tortu.penup()
    tortu.goto(-625,30)
    tortu.write("A",font=("courier",15, "bold"))
    tortu.penup()
    tortu.goto(-580,40)#A->D
    tortu.pendown()
    tortu.goto(-440,-190)#D
    tortu.penup()
    tortu.goto(-510,-150)
    tortu.write("p",font=("courier",15, "bold"))
    tortu.goto(-580,40)#A->C
    tortu.pendown()
    tortu.goto(-440,40)#C
    tortu.penup()
    tortu.goto(-510,0)
    tortu.write("e",font=("courier",15, "bold"))
    tortu.goto(-620,0)#A->E
    tortu.pendown()
    tortu.goto(-620,-380)#E
    tortu.penup()
    tortu.goto(-620,-190)
    tortu.write("s",font=("courier",15, "bold"))
    tortu.goto(-620,80)#A->B
    tortu.pendown()
    tortu.goto(-620,250)#B
    tortu.circle(40)
    tortu.penup()
    tortu.goto(-625,280)
    tortu.write("B",font=("courier",15, "bold"))
    tortu.goto(-630,170)
    tortu.write("w",font=("courier",15, "bold"))
    tortu.goto(-580,290)#B->F
    tortu.pendown()
    tortu.goto(-510,290)#F
    tortu.penup()
    tortu.goto(-545,290)
    tortu.write("e",font=("courier",15, "bold"))
    tortu.goto(-470,250)#Fz 
    tortu.pendown()
    tortu.circle(40)
    tortu.penup()
    tortu.goto(-470,280)
    tortu.write("F",font=("courier",15, "bold"))
    tortu.goto(-430,290)#F->K
    tortu.pendown()
    tortu.goto(-360,290)#K
    tortu.penup()
    tortu.goto(-395,290)
    tortu.write("b",font=("courier",15, "bold"))
    tortu.goto(-320,250)#K
    tortu.pendown()
    tortu.circle(40)
    tortu.penup()
    tortu.goto(-320,280)
    tortu.write("K",font=("courier",15, "bold"))
    tortu.goto(-320,330)#K->R
    tortu.pendown()
    tortu.goto(-210 ,420)#R
    tortu.penup()
    tortu.goto(-265,375)
    tortu.write("m",font=("courier",15, "bold"))
    tortu.goto(-320,250)#K->Q
    tortu.pendown()
    tortu.goto(-210,160)#Q
    tortu.penup()
    tortu.goto(-265,205)
    tortu.write("s",font=("courier",15, "bold"))
    tortu.goto(-280,290)#K->P
    tortu.pendown()
    tortu.goto(-210,290)#P
    tortu.penup()
    tortu.goto(-245,290)
    tortu.write("p",font=("courier",15, "bold"))
    tortu.goto(-170,250)#P
    tortu.pendown()
    tortu.circle(40)
    tortu.penup()
    tortu.goto(-170,280)
    tortu.write("P",font=("courier",15, "bold"))
    tortu.goto(-130,290)#P->V
    tortu.pendown()
    tortu.goto(-60,290)#V
    tortu.penup()
    tortu.goto(-95,290)
    tortu.write("a",font=("courier",15, "bold"))
    tortu.goto(-20,250)#V
    tortu.pendown()
    tortu.circle(40)
    tortu.penup()
    tortu.goto(-20,280)
    tortu.write("V",font=("courier",15, "bold"))
    tortu.goto(20,290)#V->Y
    tortu.pendown()
    tortu.goto(90,290)#Y
    tortu.penup()
    tortu.goto(55,290)
    tortu.write("g",font=("courier",15, "bold"))
    tortu.goto(130,250)#Y
    tortu.pendown()
    tortu.circle(40)
    tortu.penup()
    tortu.goto(130,280)
    tortu.write("Y",font=("courier",15, "bold"))
    tortu.goto(170,290)#Y->BB
    tortu.pendown()
    tortu.goto(240,290)#BB
    tortu.penup()
    tortu.goto(205,290)
    tortu.write("e",font=("courier",15, "bold"))
    tortu.goto(280,250)#BB
    tortu.pendown()
    tortu.circle(40)
    tortu.penup()
    tortu.goto(280,280)
    tortu.write("BB",font=("courier",15, "bold"))

    tortu.penup()
    tortu.goto(-170,380)#R
    tortu.pendown()
    tortu.circle(40)
    tortu.penup()
    tortu.goto(-170,410)
    tortu.write("R",font=("courier",15, "bold"))
    tortu.goto(-130,420)#R->X
    tortu.pendown()
    tortu.goto(-60,420)
    tortu.penup()
    tortu.goto(-95,420)
    tortu.write("a",font=("courier",15, "bold"))
    tortu.goto(-20,380)#X
    tortu.pendown()
    tortu.circle(40)
    tortu.penup()
    tortu.goto(-20,410)
    tortu.write("X",font=("courier",15, "bold"))
    tortu.goto(20,420)#X->AA
    tortu.pendown()
    tortu.goto(90,420)
    tortu.penup()
    tortu.goto(55,420)
    tortu.write("s",font=("courier",15, "bold"))
    tortu.goto(130,380)#AA
    tortu.pendown()
    tortu.circle(40)
    tortu.penup()
    tortu.goto(130,410)
    tortu.write("AA",font=("courier",15, "bold"))
    tortu.goto(170,420)#AA->DD
    tortu.pendown()
    tortu.goto(240,420)
    tortu.penup()
    tortu.goto(205,420)
    tortu.write("t",font=("courier",15, "bold"))
    tortu.goto(280,380)#DD
    tortu.pendown()
    tortu.circle(40)
    tortu.penup()
    tortu.goto(280,410)
    tortu.write("DD",font=("courier",15, "bold"))
    tortu.goto(320,420)#DD->EE
    tortu.pendown()
    tortu.goto(390,420)
    tortu.penup()
    tortu.goto(355,420)
    tortu.write("e",font=("courier",15, "bold"))
    tortu.goto(430,380)#EE
    tortu.pendown()
    tortu.circle(40)
    tortu.penup()
    tortu.goto(430,410)
    tortu.write("EE",font=("courier",15, "bold"))
    tortu.goto(430,380)#EE->FF
    tortu.pendown()
    tortu.goto(430,330)#FF
    tortu.penup()
    tortu.goto(430,355)
    tortu.write("r",font=("courier",15, "bold"))
    tortu.goto(430,250)#FF
    tortu.pendown()
    tortu.circle(40)
    tortu.penup()
    tortu.goto(430,280)
    tortu.write("FF",font=("courier",15, "bold"))

    tortu.penup()
    tortu.goto(-170,120)#Q
    tortu.pendown()
    tortu.circle(40)
    tortu.penup()
    tortu.goto(-170,150)
    tortu.write("Q",font=("courier",15, "bold"))
    tortu.goto(-130,160)#Q->W
    tortu.pendown()
    tortu.goto(-60,160)#W
    tortu.penup()
    tortu.goto(-95,160)
    tortu.write("i",font=("courier",15, "bold"))
    tortu.goto(-20,120)#W
    tortu.pendown()
    tortu.circle(40)
    tortu.penup()
    tortu.goto(-20,150)
    tortu.write("W",font=("courier",15, "bold"))
    tortu.goto(20,160)#W->Z
    tortu.pendown()
    tortu.goto(90,160)
    tortu.penup()
    tortu.goto(55,160)
    tortu.write("t",font=("courier",15, "bold"))
    tortu.goto(130,120)#Z
    tortu.pendown()
    tortu.circle(40)
    tortu.penup()
    tortu.goto(130,150)
    tortu.write("Z",font=("courier",15, "bold"))
    tortu.goto(170,160)#Z->CC
    tortu.pendown()
    tortu.goto(240,160)
    tortu.penup()
    tortu.goto(205,160)
    tortu.write("e",font=("courier",15, "bold"))
    tortu.goto(280,120)#CC
    tortu.pendown()
    tortu.circle(40)
    tortu.penup()
    tortu.goto(280,150)
    tortu.write("CC",font=("courier",15, "bold"))

    tortu.penup()
    tortu.goto(-400,0)#C
    tortu.pendown()
    tortu.circle(40)
    tortu.penup()
    tortu.goto(-400,30)
    tortu.write("C",font=("courier",15, "bold"))
    tortu.goto(-360,40)#C->H
    tortu.pendown()
    tortu.goto(-210,40)
    tortu.penup()
    tortu.goto(-285,40)
    tortu.write("b",font=("courier",15, "bold"))
    tortu.goto(-170,0)#H
    tortu.pendown()
    tortu.circle(40)
    tortu.penup()
    tortu.goto(-170,30)
    tortu.write("H",font=("courier",15, "bold"))
    tortu.goto(-130,40)#H>M
    tortu.pendown()
    tortu.goto(90,40)
    tortu.penup()
    tortu.goto(-20,40)
    tortu.write("a",font=("courier",15, "bold"))
    tortu.goto(130,0)#M
    tortu.pendown()
    tortu.circle(40)
    tortu.penup()
    tortu.goto(130,30)
    tortu.write("M",font=("courier",15, "bold"))
    tortu.goto(170,40)#M->S
    tortu.pendown()
    tortu.goto(390,40)
    tortu.penup()
    tortu.goto(280,40)
    tortu.write("y",font=("courier",15, "bold"))
    tortu.goto(430,0)#S
    tortu.pendown()
    tortu.circle(40)
    tortu.penup()
    tortu.goto(430,30)
    tortu.write("S",font=("courier",15, "bold"))

    tortu.penup()
    tortu.goto(-400,-230)#D
    tortu.pendown()
    tortu.circle(40)
    tortu.penup()
    tortu.goto(-400,-200)
    tortu.write("D",font=("courier",15, "bold"))
    tortu.goto(-360,-190)#D->I
    tortu.pendown()
    tortu.goto(-210,-190)
    tortu.penup()
    tortu.goto(-285,-190)
    tortu.write("a",font=("courier",15, "bold"))
    tortu.goto(-170,-230)#I
    tortu.pendown()
    tortu.circle(40)
    tortu.penup()
    tortu.goto(-170,-200)
    tortu.write("I",font=("courier",15, "bold"))
    tortu.goto(-130,-190)#I->N
    tortu.pendown()
    tortu.goto(90,-190)
    tortu.penup()
    tortu.goto(-20,-190)
    tortu.write("g",font=("courier",15, "bold"))
    tortu.goto(130,-230)#N
    tortu.pendown()
    tortu.circle(40)
    tortu.penup()
    tortu.goto(130,-200)
    tortu.write("N",font=("courier",15, "bold"))
    tortu.goto(170,-190)#N->T
    tortu.pendown()
    tortu.goto(390,-190)
    tortu.penup()
    tortu.goto(280,-190)
    tortu.write("e",font=("courier",15, "bold"))
    tortu.goto(430,-230)#T
    tortu.pendown()
    tortu.circle(40)
    tortu.penup()
    tortu.goto(430,-200)
    tortu.write("T",font=("courier",15, "bold"))

    tortu.goto(-620,-460)#E
    tortu.pendown()
    tortu.circle(40)
    tortu.penup()
    tortu.goto(-620,-430)
    tortu.write("E",font=("courier",15, "bold"))
    tortu.goto(-580,-420)#E->J
    tortu.pendown()
    tortu.goto(-440,-420)
    tortu.penup()
    tortu.goto(-510,-420)
    tortu.write("i",font=("courier",15, "bold"))
    tortu.goto(-400,-460)#J
    tortu.pendown()
    tortu.circle(40)
    tortu.penup()
    tortu.goto(-400,-430)
    tortu.write("J",font=("courier",15, "bold"))
    tortu.goto(-360,-420)#J->O
    tortu.pendown()
    tortu.goto(-210,-420)
    tortu.penup()
    tortu.goto(-285,-420)
    tortu.write("t",font=("courier",15, "bold"))
    tortu.goto(-170,-460)#O
    tortu.pendown()
    tortu.circle(40)
    tortu.penup()
    tortu.goto(-170,-430)
    tortu.write("O",font=("courier",15, "bold"))
    tortu.goto(-130,-420)#O->U
    tortu.pendown()
    tortu.goto(90,-420)
    tortu.penup()
    tortu.goto(-20,-420)
    tortu.write("e",font=("courier",15, "bold"))
    tortu.goto(130,-460)#U
    tortu.pendown()
    tortu.circle(40)
    tortu.penup()
    tortu.goto(130,-430)
    tortu.write("U",font=("courier",15, "bold"))
    sleep(3)
else:
    lectura=open("lectura.txt","r")#abrir documento
    historia=open("historia.txt","w")
    encontradas=open("encontradas.txt","w")
    #Listas donde guardaremos la ubicacion donde se encontraron
    listWeb=[]
    listWeb2=[]
    listWebPage=[]
    listWebPage2=[]
    listWebSite=[]
    listWebSite2=[]
    listWebMaster=[]
    listWebMaster2=[]
    listEbay=[]
    listEbay2=[]
    listPage=[]
    listPage2=[]
    listSite=[]
    listSite2=[]
    i=0 #eje x
    k=0 #eje y
    estado="A"#Declarar estado inicial
    while 1:
        caracter=lectura.read(1)#recorrer caracter por caracter el documento
        historia.write("(" +caracter+","+estado)
        if estado == "A":
            if caracter == "w":
                estado="B"
                historia.write("->B)\n")
            elif caracter == "e":
                estado="C"
                historia.write("->C)\n")
            elif caracter == "p":
                estado="D"
                historia.write("->D)\n")
            elif caracter == "s":
                estado = "E"
                historia.write("->E)\n")
            else:
                estado="A"
                historia.write("->A)\n")
        elif estado == "B":
            if caracter == "w":
                estado="B"
                historia.write("->B)\n")
            elif caracter == "p":
                estado="D"
                historia.write("->D)\n")
            elif caracter == "s":
                estado = "E"
                historia.write("->E)\n")
            elif caracter == "e":
                estado="F"
                historia.write("->F)\n")
            else:
                estado="A"
                historia.write("->A)\n")
        elif estado == "C":
            if caracter == "w":
                estado="B"
                historia.write("->B)\n")
            elif caracter == "e":   
                estado="C"
                historia.write("->C)\n")
            elif caracter == "p":
                estado="D"
                historia.write("->D)\n")
            elif caracter == "s":
                estado = "E"
                historia.write("->E)\n")
            elif caracter == "b":
                estado = "H"    
                historia.write("->H)\n")
            else:
                estado="A"
                historia.write("->A)\n")
        elif estado == "D":
            if caracter == "w":
                estado="B"
                historia.write("->B)\n")
            elif caracter == "e":
                estado="C"
                historia.write("->C)\n")
            elif caracter == "p":
                estado="D"
                historia.write("->D)\n")
            elif caracter == "s":
                estado = "E"
                historia.write("->E)\n")
            elif caracter == "a":
                estado = "I"
                historia.write("->I)\n")    
            else:
                estado="A"
                historia.write("->A)\n")
        elif estado == "E":
            if caracter == "w":
                estado="B"
                historia.write("->B)\n")
            elif caracter == "e":
                estado="C"
                historia.write("->C)\n")
            elif caracter == "p":
                estado="D"
                historia.write("->D)\n")
            elif caracter == "s":
                estado = "E"
                historia.write("->E)\n")
            elif caracter == "i":
                estado = "J"    
                historia.write("->A)\n")
            else:
                estado="A"
                historia.write("->A)\n")
        elif estado == "F":
            if caracter == "w":
                estado = "B"
                historia.write("->B)\n")
            elif caracter == "e":
                estado = "C"
                historia.write("->C)\n")
            elif caracter == "p":
                estado = "D"
                historia.write("->D)\n")
            elif caracter == "s":
                estado = "E"
                historia.write("->E)\n")
            elif caracter == "b":
                estado = "K" 
                historia.write("->K)\n")  
            else:
                estado="A"
                historia.write("->A)\n")
        elif estado == "H":
            if caracter == "w":
                estado="B"
                historia.write("->B)\n")
            elif caracter == "e":
                estado="C"
                historia.write("->C)\n")
            elif caracter == "p":
                estado="D"
                historia.write("->D)\n")
            elif caracter == "s":
                estado = "E"
                historia.write("->E)\n")
            elif caracter == "a":
                estado = "M"  
                historia.write("->M)\n")  
            else:
                estado="A"
                historia.write("->A)\n")
        elif estado == "I":
            if caracter == "w":
                estado="B"
                historia.write("->B)\n")
            elif caracter == "e":
                estado="C"
                historia.write("->C)\n")
            elif caracter == "p":
                estado="D"
                historia.write("->D)\n")
            elif caracter == "s":
                estado = "E"
                historia.write("->E)\n")
            elif caracter == "g":
                estado = "N"    
                historia.write("->N)\n")
            else:
                estado="A"
                historia.write("->A)\n")
        elif estado == "J":
            if caracter == "w":
                estado = "B"
                historia.write("->B)\n")
            elif caracter == "e":
                estado = "C"
                historia.write("->C)\n")
            elif caracter == "p":
                estado="D"
                historia.write("->D)\n")
            elif caracter == "s":
                estado = "E"
                historia.write("->E)\n")
            elif caracter == "t":
                estado = "O"   
                historia.write("->O)\n") 
            else:
                estado="A"
                historia.write("->A)\n")
        elif estado == "K":#Estado final
            listWeb.append(i-3)#guardar eje x
            listWeb2.append(k)#guardar eje y
            if caracter == "w":
                estado="B"
                historia.write("->B)\n")
            elif caracter == "e":
                estado="C"
                historia.write("->C)\n")
            elif caracter == "m":
                estado = "R"
                historia.write("->R)\n")
            elif caracter == "p":
                estado = "P"
                historia.write("->P)\n")
            elif caracter == "s":
                estado = "Q"   
                historia.write("->Q)\n") 
            else:
                estado="A"
                historia.write("->A)\n")
        elif estado == "M":
            if caracter == "w":
                estado="B"
                historia.write("->B)\n")
            elif caracter == "e":
                estado="C"
                historia.write("->C)\n")
            elif caracter == "p":
                estado="D"
                historia.write("->D)\n")
            elif caracter == "s":
                estado = "E"
                historia.write("->E)\n")
            elif caracter == "y":
                estado = "S"   
                historia.write("->S*)\n") 
            else:
                estado="A"
                historia.write("->A)\n")
        elif estado == "N":
            if caracter == "w":
                estado="B"
                historia.write("->B)\n")
            elif caracter == "p":
                estado="D"
                historia.write("->D)\n")
            elif caracter == "s":
                estado = "E"
                historia.write("->E)\n")
            elif caracter == "e":
                estado = "T"    
                historia.write("->T*)\n")
            else:
                estado="A"
                historia.write("->A)\n")
        elif estado == "O":
            if caracter == "w":
                estado="B"
                historia.write("->B)\n")
            elif caracter == "p":
                estado="D"
                historia.write("->D)\n")
            elif caracter == "s":
                estado = "E"
                historia.write("->E)\n")
            elif caracter == "e":
                estado = "U"    
                historia.write("->U*)\n")
            else:
                estado="A"
                historia.write("->A)\n")
        elif estado == "P":
            if caracter == "w":
                estado="B"
                historia.write("->B)\n")
            elif caracter == "e":
                estado="C"
                historia.write("->C)\n")
            elif caracter == "p":
                estado="D"
                historia.write("->D)\n")
            elif caracter == "s":
                estado = "E"
                historia.write("->E)\n")
            elif caracter == "a":
                estado = "V"    
                historia.write("->V)\n")
            else:
                estado="A"
                historia.write("->A)\n")
        elif estado == "Q":
            if caracter == "w":
                estado="B"
                historia.write("->Q)\n")
            elif caracter == "e":
                estado="C"
                historia.write("->C)\n")
            elif caracter == "p":
                estado="D"
                historia.write("->D)\n")
            elif caracter == "s":
                estado = "E"
                historia.write("->E)\n")
            elif caracter == "i":
                estado = "W"    
                historia.write("->W)\n")
            else:
                estado="A"
                historia.write("->A)\n")
        elif estado == "R":
            if caracter == "w":
                estado="B"
                historia.write("->B)\n")
            elif caracter == "e":
                estado="C"
                historia.write("->C)\n")
            elif caracter == "p":
                estado="D"
                historia.write("->D)\n")
            elif caracter == "s":
                estado = "E"
                historia.write("->E)\n")
            elif caracter == "a":
                estado = "X"    
                historia.write("->X)\n")
            else:
                estado="A"
                historia.write("->A)\n")
        elif estado == "S":#Estado Final
            listEbay.append(i-4)
            listEbay2.append(k)
            if caracter == "w":
                estado="B"
                historia.write("->B)\n")
            elif caracter == "e":
                estado="C"
                historia.write("->C)\n")
            elif caracter == "p":
                estado="D"
                historia.write("->D)\n")
            elif caracter == "s":
                estado = "E" 
                historia.write("->E)\n")
            else:
                estado="A"
                historia.write("->A)\n")
        elif estado == "T":#Estado Final
            listPage.append(i-4)
            listPage2.append(k)
            if caracter == "w":
                estado="B"
                historia.write("->W)\n")
            elif caracter == "e":
                estado="C"
                historia.write("->C)\n")
            elif caracter == "p":
                estado="D"
                historia.write("->D)\n")
            elif caracter == "s":
                estado = "E"
                historia.write("->E)\n")
            elif caracter == "b":
                estado = "H"    
                historia.write("->H)\n")
            else:
                estado="A"
                historia.write("->A)\n")
        elif estado == "U":#Estado Final
            listSite.append(i-4)
            listSite2.append(k)
            if caracter == "w":
                estado="B"
                historia.write("->B)\n")
            elif caracter == "e":
                estado="C"
                historia.write("->C)\n")
            elif caracter == "p":
                estado="D"
                historia.write("->D)\n")
            elif caracter == "s":
                estado = "E"
                historia.write("->E)\n")
            elif caracter == "b":
                estado = "H"    
                historia.write("->H)\n")
            else:
                estado="H"
                historia.write("->H)\n")
        elif estado == "V":
            if caracter == "w":
                estado="B"
                historia.write("->B)\n")
            elif caracter == "e":
                estado="C"
                historia.write("->C)\n")
            elif caracter == "p":
                estado="D"
                historia.write("->D)\n")
            elif caracter == "s":
                estado = "E"
                historia.write("->E)\n")
            elif caracter == "g":
                estado = "Y"    
                historia.write("->Y)\n")
            else:
                estado="A"
                historia.write("->A)\n")
        elif estado == "W":
            if caracter == "w":
                estado="B"
                historia.write("->B)\n")
            elif caracter == "e":
                estado="C"
                historia.write("->C)\n")
            elif caracter == "p":
                estado="D"
                historia.write("->D)\n")
            elif caracter == "s":
                estado = "E"
                historia.write("->E)\n")
            elif caracter == "t":
                estado = "Z"    
                historia.write("->Z)\n")
            else:
                estado="A"
                historia.write("->A)\n")
        elif estado == "X":
            if caracter == "w":
                estado="B"
                historia.write("->B)\n")
            elif caracter == "e":
                estado="C"
                historia.write("->C)\n")
            elif caracter == "p":
                estado="D"
                historia.write("->D)\n")
            elif caracter == "s":
                estado = "AA"    
                historia.write("->AA)\n")
            else:
                estado="A"
                historia.write("->A)\n")
        elif estado == "Y":
            if caracter == "w":
                estado="B"
                historia.write("->B)\n")
            elif caracter == "p":
                estado="D"
                historia.write("->D)\n")
            elif caracter == "s":
                estado = "E"
                historia.write("->E)\n")
            elif caracter == "e":
                estado = "BB"    
                historia.write("->BB*)\n")
            else:
                estado="A"
                historia.write("->A)\n")
        elif estado == "Z":
            if caracter == "w":
                estado="B"
                historia.write("->B)\n")
            elif caracter == "p":
                estado="D"
                historia.write("->D)\n")
            elif caracter == "s":
                estado = "E"
                historia.write("->E)\n")
            elif caracter == "e":
                estado = "CC"    
                historia.write("->CC*)\n")
            else:
                estado="A"
                historia.write("->A)\n")
        elif estado == "AA":
            if caracter == "w":
                estado="B"
                historia.write("->B)\n")
            elif caracter == "e":
                estado="C"
                historia.write("->C)\n")
            elif caracter == "p":
                estado="D"
                historia.write("->D)\n")
            elif caracter == "s":
                estado = "E"
                historia.write("->E)\n")
            elif caracter == "t":
                estado = "DD"
                historia.write("->DD)\n")
            elif caracter == "i":
                estado = "J"    
                historia.write("->J)\n")
            else:
                estado="A"
                historia.write("->A)\n")
        elif estado == "BB":#Estado Final
            listWebPage.append(i-7)
            listWebPage2.append(k)
            listPage.append(i-4)
            listPage2.append(k)
            if caracter == "w":
                estado = "B"
                historia.write("->B)\n")
            elif caracter == "e":
                estado = "C"
                historia.write("->C)\n")
            elif caracter == "p":
                estado = "D"
                historia.write("->D)\n")
            elif caracter == "s":
                estado = "E"
                historia.write("->E)\n")
            elif caracter == "b":
                estado = "H"
                historia.write("->H)\n")
            else:
                estado = "A"
                historia.write("->A)\n")
        elif estado == "CC":#Estado Final
            listWebSite.append(i-7)
            listWebSite2.append(k)
            listSite.append(i-4)
            listSite2.append(k)
            if caracter == "w":
                estado = "B"
                historia.write("->B)\n")
            elif caracter == "e":
                estado = "C"
                historia.write("->C)\n")
            elif caracter == "p":
                estado = "D"
                historia.write("->D)\n")
            elif caracter == "s":
                estado = "E"
                historia.write("->E)\n")
            elif caracter == "b":
                estado = "H"
                historia.write("->H)\n")
            else:
                estado = "A"
                historia.write("->A)\n")
        elif estado == "DD":
            if caracter == "w":
                estado = "B"
                historia.write("->B)\n")
            elif caracter == "p":
                estado = "D"
                historia.write("->D)\n")
            elif caracter == "s":
                estado = "E"
                historia.write("->E)\n")
            elif caracter == "e":
                estado = "EE"    
                historia.write("->EE)\n")
            else:
                estado = "A"
                historia.write("->A)\n")
        elif estado == "EE":
            if caracter == "w":
                estado = "B"
                historia.write("->B)\n")
            elif caracter == "p":
                estado = "D"
                historia.write("->D)\n")
            elif caracter == "s":
                estado = "E"
                historia.write("->E)\n")
            elif caracter == "b":
                estado = "H"
                historia.write("->H)\n")
            elif caracter == "r":
                estado = "FF"    
                historia.write("->FF*)\n")
            else:
                estado="A"
                historia.write("->A)\n")
        elif estado == "FF":#Estado Final
            listWebMaster.append(i-9)
            listWebMaster2.append(k)
            if caracter == "w":
                estado = "B"
                historia.write("->B)\n")
            elif caracter == "e":
                estado = "C"
                historia.write("->C)\n")
            elif caracter == "p":
                estado = "D"
                historia.write("->D)\n")
            elif caracter == "s":
                estado = "E" 
                historia.write("->E)\n")
            else:
                estado = "A"
                historia.write("->A)\n")
        
        if not caracter:#Si no hay es caracter es el fin
            break
        i+=1#Llevar la cuenta de caracteres eje x
        if caracter == "\n":
            k+=1
            i=0
    encontradas.write("Palabra web encontradas en el archivo y su ubicacion: \n")
    j=0
    for i,k in zip(listWeb,listWeb2):
        j+=1
        encontradas.write(str(j)+". "+str(k)+","+str(i)+"\n")
    encontradas.write("\nPalabra webPage encontradas en el archivo y su ubicacion: \n")
    j=0
    for i,k in zip(listWebPage,listWebPage2):
        j+=1
        encontradas.write(str(j)+". "+str(k)+","+str(i)+"\n")
    encontradas.write("\nPalabra WebSite encontradas en el archivo y su ubicacion: \n")
    j=0
    for i,k in zip(listWebSite,listWebSite2):
        j+=1
        encontradas.write(str(j)+". "+str(k)+","+str(i)+"\n")
    encontradas.write("\nPalabra WebMaster encontradas en el archivo y su ubicacion: \n")
    j=0
    for i,k in zip(listWebMaster,listWebMaster2): 
        j+=1
        encontradas.write(str(j)+". "+str(k)+","+str(i)+"\n")
    encontradas.write("\nPalabra Ebay encontradas en el archivo y su ubicacion: \n")
    j=0
    for i,k in zip(listEbay,listEbay2):
        j+=1
        encontradas.write(str(j)+". "+str(k)+","+str(i)+"\n")
    encontradas.write("\nPalabra Page encontradas en el archivo y su ubicacion: \n")
    j=0
    for i,k in zip(listPage,listPage2):
        j+=1
        encontradas.write(str(j)+". "+str(k)+","+str(i)+"\n")
    encontradas.write("\nPalabra Site encontradas en el archivo y su ubicacion: \n")
    j=0
    for i,k in zip(listSite,listSite2):
        j+=1
        encontradas.write(str(j)+". "+str(k)+","+str(i)+"\n")

    lectura.close()
    encontradas.close()
    historia.close()
    print("Se han encontrada todas las palabras, se encuentran en el archivo de texto encontradas.txt, la historia en el archivo historia.txt")