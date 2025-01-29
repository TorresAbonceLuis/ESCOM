import socket
import os
import string
import time

buffer_size = 1024

def conectarServidor(host, puerto):
    TCPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPClientSocket.connect((host, puerto))
    try:
        print("Conectado al servidor")
    except:
        print("Error al conectar al servidor:")
        TCPClientSocket.close()
        return None
    return TCPClientSocket

def cerrarConexion(TCPClientSocket):
    TCPClientSocket.close()

def dificultad(TCPClientSocket):
    print("Seleccione la dificultad: ")
    print("1. Principiante")
    print("2. Avanzado")
    enviar = input("Ingrese la opcion: ")
    try:
        TCPClientSocket.sendall(enviar.encode())
        if enviar == "1":
            tablero_jugador = tablero(9, 9)
        elif enviar == "2":
            tablero_jugador = tablero(16, 16)
        return tablero_jugador
    except:
        print("Error al enviar datos al servidor:")
        cerrarConexion(TCPClientSocket)

def tiro(TCPClientSocket):
    tiro = input("Ingrese la posicion del tiro: (1,a) fila, columna: ")
    TCPClientSocket.sendall(tiro.encode())
    data = TCPClientSocket.recv(buffer_size).decode()
    return tiro+","+data

def limpiaPantalla():
    os.system("cls")

def tablero(filas, columnas):
    tablero = []
    for i in range(filas):
        tablero.append([])
        for j in range(columnas):
            tablero[i].append(" ")
    return tablero

def imprimirTablero(tablero):
    limpiaPantalla()
    letras_columnas = string.ascii_lowercase[:len(tablero[0])]
    print("  " + " ".join(letras_columnas))
    for i, fila in enumerate(tablero):
        print(i + 1, end=" ")
        for celda in fila:
            print(celda, end=" ")
        print()

def actualizarTablero(tablero, fila, columna, resultado):
    if resultado == "0":
        tablero[fila][columna] = "0"
    elif resultado == "1":
        tablero[fila][columna] = "*"
    return tablero

def recibirCoordenadas(TCPClientSocket):
    data = TCPClientSocket.recv(buffer_size).decode()
    return data

def minasTablero(TCPClientSocket, tablero):
    coordenadas = recibirCoordenadas(TCPClientSocket)
    coordenadas = eval(coordenadas)
    print(coordenadas)
    for tupla in coordenadas:
        fila, columna = tupla
        tablero[fila][columna] = "*"

def main():
    limpiaPantalla()
    TCPClientSocket = conectarServidor("localhost", 65432)
    if TCPClientSocket is not None:
        tablero_jugador= dificultad(TCPClientSocket)
        limpiaPantalla()
        imprimirTablero(tablero_jugador)
        while True:
            resultado = tiro(TCPClientSocket)
            fila, columna, resultado = resultado.split(',')
            fila = int(fila) - 1
            columna = string.ascii_lowercase.index(columna)
            tablero_jugador = actualizarTablero(tablero_jugador, fila, columna, resultado)
            imprimirTablero(tablero_jugador)
            if resultado == "1":
                print("Perdiste :(")
                minasTablero(TCPClientSocket, tablero_jugador)
                imprimirTablero(tablero_jugador)
                break
            elif resultado == "2":
                print("Ganaste :)")
                break
            elif resultado == "0":
                print("Sigue jugando")
        data = TCPClientSocket.recv(buffer_size).decode()
        print("Tiempo de partida: ", data)

main()
