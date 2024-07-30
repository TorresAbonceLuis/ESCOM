import os
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def AjustarNum(numero):
    while len(numero)%2!=0:
        numero='0'+numero
    return numero

def comprobarTamanio(num1,num2):
    while len(num1)!=len(num2):
        if(len(num2)>len(num1)):
            num1='0'+ num1
        else:
            num2='0'+num2
    num1=AjustarNum(num1)
    num2=AjustarNum(num2)
    return(num1,num2)    

def comprobarBinario(num):
    i=0
    while(i!=len(num)):
        if '1' in num[i]:
            i=i+1
        elif '0' in num[i]:
            i=i+1
        else:
            return 1
    return 0

def dividirMitad(num):
    num1, num2 = num[:int(len(num)/2)], num[int(len(num)/2):]
    return (num1,num2)

def binarioDecimal(numero):
	decimal=0 
	for posicion, digito_string in enumerate(numero[::-1]):
		decimal += int(digito_string) * 2 ** posicion
	return decimal
    
def principal(): #En este apartado lo unico que se realiza es la captura de los datos que se utilizaran a lo largo del programa
    z=1
    y=1
    while(z==1):
        while(y==1):        
            print('Cual es la base de los numeros')
            print('1.binario\n2.decimal\n3.Hexadecimal\nSelecciona una opcion:')
            base=input()
            base=int(base)
            if base>0 and base<4:
                print('entro')
                y=0
            else:
                clearConsole()
                print('Introduce un valor valido')
        clearConsole()
        print('Primer numero a multiplicar: ')
        numero1=input()
        print('Segundo numero a multiplicar:')
        numero2=input()
        clearConsole()
        if(base==1):
            y=comprobarBinario(numero1)
            if(y==0):
                y=comprobarBinario(numero2)
                if(y==0):
                    z=0
            elif(y==1):
                print('Introduce numeros binarios (1s y 0s)')
        elif(base==2):
            try:
                int(numero1,16)
                int(numero2,16)
                z=0
            except:
                print('Introduce un numero correcto')
                y=1
                z=1
        else:
            import string
            if(all(c in string.hexdigits for c in numero1+numero2)):
                z=0
            else:
                print('Introduce un numero hexadecimal valido')
                y=1
                z=1
    if(base==1):
        print("La multiplicacion de "+numero1+" X "+numero2)
        numero1=binarioDecimal(numero1)
        numero2=binarioDecimal(numero2)
        numero1=str(numero1)
        numero2=str(numero2)
        numero1,numero2=comprobarTamanio(numero1,numero2)
        resultado=divideYVenceras(numero1,numero2)
        resultado=format(int(resultado), "b")
        print("resultado: "+str(resultado))
    elif(base==2):
        print("La multiplicacion de "+numero1+" X "+numero2)
        (numero1,numero2)=comprobarTamanio(numero1,numero2)
        resultado=divideYVenceras(numero1,numero2)
        print("resultado: "+str(int(resultado)))
    elif(base==3):
        print("La multiplicacion de "+numero1+" X "+numero2)
        numero1=int(numero1,16)
        numero2=int(numero2,16)
        (numero1,numero2)=comprobarTamanio(str(numero1),str(numero2))
        resultado=divideYVenceras(numero1,numero2)
        resultado=hex(int(resultado)).split('x')[-1]
        print("resultado: "+str(resultado))

def casoBase(num1,num2):
    if(len(num1)==1 and len(num2)==1):
        return True
    return False

def divideYVenceras(numero1,numero2):
    if casoBase(numero1,numero2):
        return int (numero1)*int(numero2) 
    else:
        numero1,numero2=comprobarTamanio(numero1,numero2)
        xi,xd=dividirMitad(numero1)
        yi,yd=dividirMitad(numero2)
        p1=divideYVenceras(xi,yi)
        p2=divideYVenceras(suma(xi,xd),suma(yi,yd))
        p3=divideYVenceras(xd,yd)
        n=len(numero1)
        Resultado=(pow(10,n)*p1)+(pow(10,n/2)*(p2-p1-p3))+p3
    return Resultado

def suma(num1,num2):
    result=int(num1)+int(num2)
    result=str(result)
    return result

clearConsole()
principal()