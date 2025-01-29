import random

def crear_tablero(filas, columnas, minas):
    tablero = [[' ' for _ in range(columnas)] for _ in range(filas)]
    
    # Coloca las minas en posiciones aleatorias
    for _ in range(minas):
        fila, columna = random.randint(0, filas - 1), random.randint(0, columnas - 1)
        while tablero[fila][columna] == 'X':
            fila, columna = random.randint(0, filas - 1), random.randint(0, columnas - 1)
        tablero[fila][columna] = 'X'
    
    # Calcula los números alrededor de las minas
    for fila in range(filas):
        for columna in range(columnas):
            if tablero[fila][columna] == ' ':
                minas_alrededor = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if 0 <= fila + i < filas and 0 <= columna + j < columnas and tablero[fila + i][columna + j] == 'X':
                            minas_alrededor += 1
                if minas_alrededor > 0:
                    tablero[fila][columna] = str(minas_alrededor)
    
    return tablero

def imprimir_tablero(tablero):
    for fila in tablero:
        print(' '.join(fila))

def destapar_casilla(tablero, tablero_visible, fila, columna):
    if tablero_visible[fila][columna] != ' ':
        return
    
    filas, columnas = len(tablero), len(tablero[0])
    stack = [(fila, columna)]

    while stack:
        fila, columna = stack.pop()
        
        if tablero[fila][columna] == 'X':
            continue
        
        minas_alrededor = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= fila + i < filas and 0 <= columna + j < columnas and tablero[fila + i][columna + j] == 'X':
                    minas_alrededor += 1
        
        if minas_alrededor > 0:
            tablero_visible[fila][columna] = str(minas_alrededor)
        else:
            tablero_visible[fila][columna] = ' '
            
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= fila + i < filas and 0 <= columna + j < columnas and tablero_visible[fila + i][columna + j] == ' ':
                        stack.append((fila + i, columna + j))

def jugar():
    filas = 9
    columnas = 9
    minas = 10
    tablero = crear_tablero(filas, columnas, minas)
    tablero_visible = [[' ' for _ in range(columnas)] for _ in range(filas)]
    juego_terminado = False
    
    while not juego_terminado:
        imprimir_tablero(tablero_visible)
        fila = int(input("Ingrese la fila (0-8): "))
        columna = int(input("Ingrese la columna (0-8): "))
        
        if tablero[fila][columna] == 'X':
            print("¡Has perdido!")
            juego_terminado = True
        else:
            destapar_casilla(tablero, tablero_visible, fila, columna)
            casillas_destapadas = sum(row.count(' ') for row in tablero_visible)
            if casillas_destapadas == filas * columnas - minas:
                print("¡Has ganado!")
                juego_terminado = True

if __name__ == "__main__":
    jugar()