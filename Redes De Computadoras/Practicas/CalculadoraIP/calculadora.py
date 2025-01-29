from tkinter import *
from tkinter import messagebox
import re

# Crear ventana
calculadora = Tk()
calculadora.title("CalculadoraIP")
calculadora.geometry("300x200")
calculadora.configure(background="white")


#clase para subredes
class Subred:
    network = ""
    host_min = ""
    host_max = ""
    broadcast = ""
    NoHosts = 0

def limpiar():#limpiar los campos
    E1.delete(0,END)
    E2.delete(0,END)
    E3.delete(0,END)

def calcular():# Obtener valores de los Entry
    netmask = E2.get()
    address = E1.get() 
    move_to = E3.get()

    # Validar que los valores no esten vacios
    try:
        if netmask == "" or address == "":#verificar que los campos no esten vacios
            messagebox.showerror("Error", "Debe llenar todos los campos")
        regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
        if not re.match(regex, address):#verificar si la direccion ip es valida
            messagebox.showerror("Error", "La direccion IP no es valida")
            return
        if not int(netmask) in range(1, 33):#verificar si la mascara es valida
            messagebox.showerror("Error", "La mascara de red no es valida")
            return
        if move_to == "":#verificar que el campo no este vacio
            move_to= "no"
        elif not int(move_to) in range(1, 33):#verificar si move_to es valido
            messagebox.showerror("Error", "El valor de move_to no es valido")
            return
    except:
        return
    #convertir a enteros los valores
    netmask = int(netmask)
    if move_to != "no":
        move_to = int(move_to)

    #Verificar la clase de la direccion ip
    if int(address.split(".")[0]) in range(1, 128):
        clase = "A"
    elif int(address.split(".")[0]) in range(128, 192):
        clase = "B"
    elif int(address.split(".")[0]) in range(192, 224):
        clase = "C"
    elif int(address.split(".")[0]) in range(224, 240):
        clase = "D"
    elif int(address.split(".")[0]) in range(240, 256):
        clase = "E"

    #obtener la direccion de red binaria
    address_bin = ""
    j=0
    for i in address.split("."):
        address_bin += bin(int(i))[2:].zfill(8)
        if (j!=3):
            address_bin += "."
        j+=1

    #obtener la mascara de red binaria
    netmask_bin = ""#declarar mascara binaria vacia
    for i in range(0, netmask):
        netmask_bin = netmask_bin + "1"
        if i == 7 or i == 15 or i == 23:
            if i == netmask - 1:
                break
            netmask_bin = netmask_bin + "."#agregar un punto cada 8 bits
    while(i!=31):
        if i == 7 or i == 15 or i == 23:
            if i != 31:
                netmask_bin = netmask_bin + "."
            else:    
                break
        netmask_bin = netmask_bin + "0"
        i = i + 1

    #obtener la wildcard
    wildcard = ""
    i=0
    for i in netmask_bin.split("."):
        wildcard += str(255 - int(i, 2))
        wildcard += "."
    wildcard = wildcard[:-1]

    #obtener la wildcard binaria
    wildcard_binaria = ""
    for i in wildcard.split("."):
        wildcard_binaria += bin(int(i))[2:].zfill(8)
        wildcard_binaria += "."
    wildcard_binaria = wildcard_binaria[:-1]

    #obtener network_bin
    i=netmask
    network_bin=address_bin[:i+2]
    i+=2
    while i!=len(address_bin):
        if address_bin[i]!='.':
            network_bin+='0'
        else:
            network_bin=network_bin+'.'
        i+=1

    #obtener network
    network = ""
    i=0
    j=0
    for i in network_bin.split("."):
        network += str(int(i, 2))
        if(j!=3):
            network += "."
        j+=1

    NoHosts = 2**(32 - netmask)-2

    HostMin_bin=network_bin[:-1]
    HostMin_bin+='1'
    #obtener la host minima
    HostMin = ""
    i=0
    for i in HostMin_bin.split("."):
        HostMin += str(int(i, 2))
        HostMin += "."
    HostMin = HostMin[:-1]

    #obtener HostMax_bin
    j=0
    if netmask > 8:  j+=1
    if netmask > 16: j+=1
    if netmask > 24: j+=1
    HostMax_bin=network_bin[:j+netmask]

    i=j+netmask 
    while i!=35:
        if network_bin[i]!='.':
            HostMax_bin+='1'
        else:
            HostMax_bin=HostMax_bin+'.'
        i+=1
            

    HostMax_bin=HostMax_bin[:-1]
    HostMax_bin+='0'

    #obtener la host maxima
    HostMax = ""
    i=0
    for i in HostMax_bin.split("."):
        HostMax += str(int(i, 2))
        HostMax += "."
    HostMax = HostMax[:-1]

    #obtener broadcast_bin
    broadcast_bin= HostMax_bin[:-1]
    broadcast_bin+='1'

    #obtener broadcast
    broadcast = ""
    i=0
    for i in broadcast_bin.split("."):
        broadcast += str(int(i, 2))
        broadcast += "."
    broadcast = broadcast[:-1]
    
    resultado = Tk()
    resultado.title("Resultado")
    resultado.geometry("700x500")

    #crear la scrollbar
    label=Label(resultado)
    texto=Text(label)
    texto.grid(row=0,column=0,sticky=W)
    scrollbar=Scrollbar(label, orient=VERTICAL, command=texto.yview)
    texto.config(yscrollcommand=scrollbar.set)
    scrollbar.grid(row=0,column=1,sticky=W)
    label.grid(row=0,column=0,sticky=W)
    #resultado.configure(background="white")
    texto.insert(END,"Address:      " + address +"          "+ address_bin+"\n")
    texto.insert(END,"Netmask:      " + str(netmask) +"                       "+ netmask_bin+"\n")
    texto.insert(END,"Wildcard:     " + wildcard +"             "+ wildcard_binaria+"\n")
    texto.insert(END,"--------------------------------------------------------------------------"+"\n")

    texto.insert(END,"Network:      " + network +"               "+ network_bin+"\n")
    texto.insert(END,"HostMin:      " + HostMin +"               "+ HostMin_bin+"\n")
    texto.insert(END,"HostMax:      " + HostMax +"          "+ HostMax_bin+"\n")
    texto.insert(END,"Broadcast:    " + broadcast +"          "+ broadcast_bin+"\n")
    texto.insert(END,"Hosts/net:    " + str(NoHosts)+"\n")
    texto.insert(END,"Clase:        " + clase+"\n")
    texto.insert(END,"--------------------------------------------------------------------------"+"\n")

    if move_to != "no":
        Netmask2 = int(move_to)
        #obtener la mascara de red binaria
        netmask2_bin = ""#declarar mascara binaria vacia
        for i in range(0, Netmask2):
            netmask2_bin = netmask2_bin + "1"
            if i == 7 or i == 15 or i == 23:
                if i == Netmask2 - 1:
                    break
                netmask2_bin = netmask2_bin + "."#agregar un punto cada 8 bits
        while(i!=31):
            if i == 7 or i == 15 or i == 23:
                if i != 31:
                    netmask2_bin = netmask2_bin + "."
                else:    
                    break
            netmask2_bin = netmask2_bin + "0"
            i = i + 1
        
        #obtener la wildcard2
        wildcard2 = ""
        i=0
        for i in netmask2_bin.split("."):
            wildcard2 += str(255 - int(i, 2))
            wildcard2 += "."
        wildcard2 = wildcard2[:-1]

        #obtener la wildcard binaria
        wildcard_binaria2 = ""
        for i in wildcard2.split("."):
            wildcard_binaria2 += bin(int(i))[2:].zfill(8)
            wildcard_binaria2 += "."
        wildcard_binaria2 = wildcard_binaria2[:-1]

        #obtener las subnets
        subnet = Netmask2 - netmask
        subnet_bin = ""
        for i in range(0, subnet):
            subnet_bin += "1"
        subnet_dec = int(subnet_bin,2)

        texto.insert(END,"Netmask2:     " + str(Netmask2) +"                    "+ netmask2_bin+"\n")
        texto.insert(END,"Wildcard2:    " + wildcard2 +"           "+ wildcard_binaria2+"\n"+"\n")

        i=1
        suma=[]
        string_suma=""
        acarreo=0
        binario=network.split(".")
        wildcard2=wildcard2.split(".")
        print(binario)
        print(wildcard2)
        string_suma=network
        string_hostmin2=HostMin
        for i in range(0, subnet_dec+1):
            texto.insert(END,"Subnet "+str(i+1)+":"+"\n")
            texto.insert(END,"Network:      " + string_suma +"          "+"\n")
            texto.insert(END,"HostMin:      " + string_hostmin2 +"          "+"\n")
            #calcular Host Min

            suma.clear()
            string_suma=""
            for i in range(3,-1,-1):
                if wildcard2[i]=='255':
                    suma.append(255)
                elif int(binario[i])+int(wildcard2[i])-256>=0:
                    suma.append(int(binario[i])+int(wildcard2[i])-256)
                    acarreo=1
                else:
                    if acarreo==1:
                        suma.append(int(binario[i])+int(wildcard2[i])+1)
                        acarreo=0
                    else:
                        suma.append(int(binario[i])+int(wildcard2[i]))
            #calcular Host Max            
            suma.reverse()
            for i in suma:
                string_suma+=str(i)+"."
            string_suma=string_suma[:-1]
            #host maximo
            i=0
            binario=string_suma.split(".")
            string_hostmax2=""
            for i in range(3,-1,-1):
                if binario[i]!='255':
                    binario[i]=(int(binario[i])-1)
                    break 
                else:
                    binario[i]=254
            for i in binario:
                string_hostmax2+=str(i)+"."
            string_hostmax2=string_hostmax2[:-1]
            texto.insert(END,"HostMax:      " + string_hostmax2 +"          "+"\n")
            texto.insert(END,"Broadcast:    " + string_suma+"\n")
            
            #calcular Host min
            i=0
            binario=string_suma.split(".")
            suma.clear()
            string_suma=""
            for i in range(3,-1,-1):
                if binario[i]!='255':
                    binario[i]=(int(binario[i])+1)
                    break 
                else:
                    binario[i]=0
            for i in binario:
                string_suma+=str(i)+"."
            string_suma=string_suma[:-1]

            #host minimo
            i=0
            binario=string_suma.split(".")
            string_hostmin2=""
            for i in range(3,-1,-1):
                if binario[i]!='255':
                    binario[i]=(int(binario[i])+1)
                    break 
                else:
                    binario[i]=0
            for i in binario:
                string_hostmin2+=str(i)+"."
            string_hostmin2=string_hostmin2[:-1]


            binario=string_suma.split(".")
                
    texto.configure(state="disabled")

#crear label y entry de address
L1=Label(calculadora, text="Address(Host or Network)",bg="white").grid(row=0,column=0,sticky=W)
E1=Entry(calculadora, bd =1, bg="white")
E1.grid(row=0,column=1,sticky=W)
#crear label y entry de netmask
L2=Label(calculadora, text="Netmask(i.e. 24)",bg="white").grid(row=1,column=0,sticky=W)
E2=Entry(calculadora, bd =1,bg="white")
E2.grid(row=1,column=1,sticky=W)
#crear label y entry de move_to
L3=Label(calculadora, text="Move to:",bg="white").grid(row=2,column=0,sticky=W)
E3=Entry(calculadora, bd =1, bg="white")
E3.grid(row=2,column=1,sticky=W)
# Crear botones
B1=Button(calculadora, text="Calcular",command=calcular,bg="white").grid(row=3,column=0,sticky=W)
B2=Button(calculadora, text="limpiar",command=limpiar,bg="white").grid(row=3,column=1,sticky=W)

calculadora.mainloop()