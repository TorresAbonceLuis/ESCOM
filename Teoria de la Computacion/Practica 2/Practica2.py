from random import randint#librerias a utilizar
from math import log10
def conversion(num):#convertir un numero a binario
    bin = 0
    i=0
    x=1
    while num != 0:#mientras num sea dif 0 
        bin=bin+num%2*x#
        num //= 2# se obtiene el cociente de la division
        x*= 10
        i+=1
    return bin,i# se regresa el num bin y longt

def esprimo(n,m):#verificar si es primo o no
    x=2
    while(x!=n):#recorrer todos los numeros desde 0 a n
        if(n%x==0):# determinar si es primo
            return 0# no es primo
        x+=1
    (n,i)=conversion(n)#Se convierte el numero
    f.write(str(n)+",")#Se escribe en archivos
    g.write(str(i)+","+str(m)+"\n")
    g10.write(str(m)+","+str(round(log10(i),2))+"\n")
    h.write(str(str(n).count("1"))+","+str(m)+"\n")
    h10.write(str(round(log10(str(n).count("1")),2))+","+str(m)+"\n")
    return 1

f=open('binario.txt','w')#Se abren los archivos
g=open('simbolos.csv','w')
g10=open('simbolo10.csv','w')
h=open('unos.csv','w')
h10=open('unos10.csv','w')
j=1
print("\nMenu del Programa numeros primos en su forma binaria")
print("1. Asignar un valor")
print("2. Dar un valor aleatorio")
opcion=int(input("Elige una opcion: "))
if(opcion==2):# se asgina valor aleatoria a n
    n=randint(0,5)
else:
    n=int(input("Valor de n: "))# se asigna valora a n
x=2
while(x!=n):#mandar todos los numero a verificar de 2 a n
    if(esprimo(x,j)==1):
        j+=1# numero de cadena
    x+=1
f.close()# se cierran los archivos
g.close()
g10.close()
h.close()
h10.close()