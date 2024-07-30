cadena="Hola como estan"
x=0
for i in cadena:
    cadena2=cadena[:x]
    cadena2=cadena2+str(x)
    cadena2=cadena2+cadena[x+1:]
    print(cadena2)
    cadena=cadena2
    x+=1

cadena2=cadena[:3]
print(cadena2)
cadena2=cadena2+"Y"
cadena2=cadena2+cadena[3+1:]
print(cadena2)
cadena=cadena2