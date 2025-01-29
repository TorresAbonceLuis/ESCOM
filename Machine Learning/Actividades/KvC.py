import numpy as np


# Generar datos sintéticos para 'edad' y 'credito'
edades = np.random.randint(18, 60 + 1, 200)
creditos = np.random.randint(3000, 1000000 + 1, 200)

# Generar la clase 
cumplio = np.random.randint(0, 2, 200)

# Guardar los datos en un archivo de texto
with open('datos_clientes.csv', 'w') as archivo:
    archivo.write("edad,credito,cumplio\n") 
    for i in range(200):
        archivo.write(f"{edades[i]},{creditos[i]},{cumplio[i]}\n")
        
