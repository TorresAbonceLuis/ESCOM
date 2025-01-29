import itertools
import random

def matrizAleatoria():
    filas = 3
    columnas = 3
    numeros = list(range(1, 10))  # Lista del 1 al 9
    random.shuffle(numeros)  # Mezclar los números
    matriz = []
    indice = 0
    for i in range(filas):
        fila = []
        for j in range(columnas):
            # Tomar el siguiente número de la lista mezclada
            fila.append(numeros[indice])
            indice += 1
        matriz.append(fila)
    return matriz

def verificarSolucion(matriz):
    # Verificar que todas las filas, columnas y diagonales sumen lo mismo
    suma_objetivo = sum(matriz[0])
    for fila in matriz:
        if sum(fila) != suma_objetivo:
            return False
    for columna in range(3):
        if sum(matriz[fila][columna] for fila in range(3)) != suma_objetivo:
            return False
    if sum(matriz[i][i] for i in range(3)) != suma_objetivo:
        return False
    if sum(matriz[i][2-i] for i in range(3)) != suma_objetivo:
        return False
    return True

def generarMovimientos(matriz):
    movimientos = []
    for (i, j), (x, y) in itertools.combinations(itertools.product(range(3), repeat=2), 2):#obtener combinaciones
        nuevo = [fila[:] for fila in matriz]
        nuevo[i][j], nuevo[x][y] = nuevo[x][y], nuevo[i][j]
        movimientos.append(nuevo)
    return movimientos

def busquedaProfundidad(matriz, camino, profundidad_maxima):
    if verificarSolucion(matriz):#si es solucion
        return camino + [matriz]#regresa camino
    if len(camino) >= profundidad_maxima:#si estamos en la profundidad maxima
        return None#regresa None
    for siguiente in generarMovimientos(matriz):#obtener movimientos
        if siguiente not in camino:# no repetir movimientos
            resultado = busquedaProfundidad(siguiente, camino + [siguiente], profundidad_maxima)#buscar solucion
            if resultado:#solucion
                return resultado#regresa resultado
    return None

#matriz_inicial = [
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9]
#]
def main ():
    matriz_inicial = matrizAleatoria()
    print("Matriz inicial:")
    for fila in matriz_inicial:
        print(fila)
    profundidad_maxima = 7

    camino = busquedaProfundidad(matriz_inicial, [matriz_inicial], profundidad_maxima)
    if camino:
        print("Camino:")
        pas=1
        for paso, matriz in enumerate(camino):
            print(f"Paso {paso}:")
            for fila in matriz:
                print(fila)
            print()
    else:
        print("No se encontró solución.")

main()