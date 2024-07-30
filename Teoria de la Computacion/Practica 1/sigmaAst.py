import random
from math import log10

def combinacion(n,x):
    for i in range(2**n):
        a=format(i,"b").zfill(n)
        f.write(a+",")
        simbolos.write(str(x)+","+str(n)+"\n")
        simbolos10.write(str(x)+","+str(log10(n))+"\n")
        unos.write(str(x)+","+str(a.count("1"))+"\n")
        try:
            unos10.write(str(x)+","+str(log10(a.count("1")))+"\n")
        except:
            unos10.write(str(x)+","+"0"+"\n")
        x+=1
    return x

opcion=5
while opcion!=1:
    print ("\tMenu del programa")
    print("1. Dar valor a n")
    print("2. Dar valor a n aleatorio")
    opcion=int(input("Seleccione una opcion: "))
    if opcion==1:
        n=int(input("Valor de n: "))
    elif opcion==2:
        n=random.randint(1,5)
        print("El valor de n es: "+str(n))
    n+=1
    f=open('universo.txt','w')
    simbolos=open('simbolos.csv','w')
    simbolos10=open('simbolos10.txt','w')
    f.write('E^'+str(n-1)+'= ')
    f.write('{')
    unos=open('unos.txt','w')
    unos10=open('unos10.txt','w')
    x=1
    l=0
    while x!=n:
        l=combinacion(x,l)
        x+=1
    f.write('}')
    f.close()
    simbolos.close()
    simbolos10.close()
    unos.close()
    unos10.close()
    opcion=int(input("Quieres Calcular otra n (1=no, 0=si): "))
    if(opcion==0):
        print("Hasta luego")