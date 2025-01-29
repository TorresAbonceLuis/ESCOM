import numpy as np

# Generar datos sintéticos para 'Duración de la canción', 'Género musical', 'Número de artistas' y 'Número de reproducciones'
duracionCancion = np.random.randint(180, 600 + 1, 200) # Duración de la canción de 180 segundos a 600 segundos
generoMusical = np.random.randint(0, 4, 200) # Género musical, 0 a 4 representando 5 géneros diferentes
numeroArtistas = np.random.randint(1, 5 + 1, 200) # Número de artistas, de 1 a 5
numeroReproducciones = np.random.randint(1000, 1000000 + 1, 200) # Número de reproducciones, de 1000 a 1000000

# Guardar los datos en un archivo de texto
with open('datos_musica.csv', 'w') as archivo:
    archivo.write("Duración de la Canción,Género Musical,Número de Artistas,Número de Reproducciones\n") 
    for i in range(200):
        archivo.write(f"{duracionCancion[i]},{generoMusical[i]},{numeroArtistas[i]},{numeroReproducciones[i]}\n")
