import socket
import os
import string
import time
import threading
from queue import Queue
import queue
import sys

buffer_size = 1024
mensaje_queue = Queue()  # Cola para manejar mensajes

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

def tiro(TCPClientSocket):
    tiro = input("Ingrese la posición del tiro: (1,a) fila, columna: ")
    TCPClientSocket.sendall(tiro.encode())
    while not mensaje_queue.empty():
        ultimo_mensaje = mensaje_queue.get(timeout=.1)
        if ultimo_mensaje == "fin":
            return ultimo_mensaje
    data = mensaje_queue.get()
    while not mensaje_queue.empty():
        ultimo_mensaje = mensaje_queue.get(timeout=.1)
    if data == "desconexion":
            limpiaPantalla()
            print("Alguien mas se ha desconectando, el juego ha terminado")
    if data == "fin":
        return data
    return tiro + ","+ data

def limpiaPantalla():
    os.system("cls")

def imprimirTablero(tablero):
    #limpiaPantalla()
    letras_columnas = string.ascii_lowercase[:len(tablero[0])]
    print("  " + " ".join(letras_columnas))
    for i, fila in enumerate(tablero):
        print(i + 1, end=" ")
        for celda in fila:
            print(celda, end=" ")
        print()

def tablero(filas, columnas):
    tablero = []
    for i in range(filas):
        tablero.append([])
        for j in range(columnas):
            tablero[i].append(" ")
    return tablero

def actualizarTablero(tablero, fila, columna, resultado):
    if resultado == "1" or resultado == "2":
        tablero[fila][columna] = "0"
    elif resultado == "0":
        tablero[fila][columna] = "*"
    return tablero

def recibirCoordenadas(TCPClientSocket):
    while not mensaje_queue.empty():
        ultimo_mensaje = mensaje_queue.get(timeout=.1)
    return ultimo_mensaje

def minasTablero(TCPClientSocket, tablero):
    coordenadas = recibirCoordenadas(TCPClientSocket)
    coordenadas = eval(coordenadas)
    for tupla in coordenadas:
        fila, columna = tupla
        tablero[int(fila)][int(columna)] = "*"

def recibirDificultad(TCPClientSocket):
    data = mensaje_queue.get()
    time.sleep(.1)  
    if data == "1": #principiante
        tableroa = tablero(9,9)
    elif data == "2": # avanzado
        tableroa = tablero(16,16)
    return tableroa

def worker(TCPClientSocket):
    while True:
        try:
            data = TCPClientSocket.recv(buffer_size).decode()
        except:
            #limpiaPantalla()
            print("El servidor se ha desconectado, el juego ha terminado")
            TCPClientSocket.close()
            mensaje_queue.put("desconexion")
            break
        if not data:
            break
        mensaje_queue.put(data)

def main():
    limpiaPantalla()
    TCPClientSocket = conectarServidor("192.168.68.108", 65432)
    t = threading.Thread(target=worker, args=(TCPClientSocket,))
    t.start()
    if TCPClientSocket is not None:
        mensaje_bienvenida = mensaje_queue.get()
        print(mensaje_bienvenida)
        tablero_jugador = recibirDificultad(TCPClientSocket)
        limpiaPantalla()
        imprimirTablero(tablero_jugador)
        i=0
        while True:
            ultimo_mensaje = None
            try:
                # Vacía la cola y conserva solo el último mensaje
                while not mensaje_queue.empty():
                    ultimo_mensaje = mensaje_queue.get(timeout=.1)
                    if ultimo_mensaje == "fin":
                        resultado = mensaje_queue.get()
                        minasTablero(TCPClientSocket, tablero_jugador)
                        imprimirTablero(tablero_jugador)
                        if resultado == "0":
                            print("Alguien más perdió :(")
                            break
                        elif resultado == "1":
                            print("Tiraste en la misma casilla")
                        elif resultado == "3":
                            print("Ganaste :)")
                            break
                        break
                # Procesa solo el último mensaje si existe
                if ultimo_mensaje is not None:
                    coordenadasTiro = eval(ultimo_mensaje)
                    for tupla in coordenadasTiro:
                        fila, columna, resultado = tupla
                        tablero_jugador = actualizarTablero(tablero_jugador, int(fila), int(columna), str(resultado))
                    imprimirTablero(tablero_jugador)
            except:
                pass
            resultado = tiro(TCPClientSocket)
            print("resultado",resultado)
            time.sleep(1)
            if resultado == "fin":
                minasTablero(TCPClientSocket, tablero_jugador)
                imprimirTablero(tablero_jugador)
                break
            print("Resultado",resultado)
            fila, columna, resultado = resultado.split(',')
            fila = int(fila) - 1
            columna = string.ascii_lowercase.index(columna)
            tablero_jugador = actualizarTablero(tablero_jugador, fila, columna, resultado)
            imprimirTablero(tablero_jugador)
            if resultado == "0":  # Perdió
                minasTablero(TCPClientSocket, tablero_jugador)
                imprimirTablero(tablero_jugador)
                print("Perdiste :(")
                break
            elif resultado == "1":  # misma casilla
                print("Tiraste en la misma casilla")
            elif resultado == "2":  # sigue jugando
                imprimirTablero(tablero_jugador)
                print("Sigue jugando")
            elif resultado == "3":  # Ganó
                print("Ganaste :)")
                break
        i+=1
    print("Se ha cerrado la conexión")
    TCPClientSocket.sendall(str("").encode())
    time.sleep(1)

if __name__ == "__main__":
    main()
