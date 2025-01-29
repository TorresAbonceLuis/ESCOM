import socket
import random
import os
import string
import time

HOST = "localhost"
PORT = 65432
buffer_size = 1024

def prenderServidor():
    TCPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPServerSocket.bind((HOST, PORT))
    TCPServerSocket.listen()
    print("El servidor está disponible")
    
    Client_conn, Client_addr = TCPServerSocket.accept()
    return Client_conn, TCPServerSocket

def apagarServidor(TCPServerSocket):
    TCPServerSocket.close()
    
def cerrarConexion(Client_conn):
    Client_conn.close()

def recibirDificultad(Client_conn):
    data = Client_conn.recv(buffer_size)
    print("El cliente eligió la dificultad: ")
    if data.decode() == "1":#Principiante
        minas = 10
        print("Principiante")
        tableros, coordenadas = tablero(9, 9, minas)
        return tableros, minas , coordenadas
    elif data.decode() == "2":#Avanzado
        minas = 40
        print("Avanzado")
        tableros, coordenadas = tablero(16, 16, minas)
        return tableros, minas, coordenadas

def tablero(filas, columnas, minas):
    tablero = []
    for i in range(filas):
        tablero.append([])
        for j in range(columnas):
            tablero[i].append(" ")
    tablero, coordenadas = agregarMinas(tablero, minas)
    return tablero, coordenadas

def agregarMinas(tablero, minas):#Agrega las minas al tablero aleatoriamente
    coordenadas = []
    for i in range(minas):
        fila = random.randint(0, len(tablero) - 1)
        columna = random.randint(0, len(tablero[0]) - 1)
        tablero[fila][columna] = "*"
        coordenadas.append((fila, columna))
    for i in range(len(coordenadas)):
        print(coordenadas[i])
    return tablero, coordenadas

def imprimirTablero(tablero):
    limpiaPantalla()
    letras_columnas = string.ascii_lowercase[:len(tablero[0])]
    print("  " + " ".join(letras_columnas))
    for i, fila in enumerate(tablero):
        print(i + 1, end=" ")
        for celda in fila:
            print(celda, end=" ")
        print()

def limpiaPantalla():
    os.system("cls")

def tiro(tablero, fila, columna):#Verifica si el tiro es válido
    if tablero[fila][columna] == "*":
        return False#Perdió
    else:
        return True

def actualizarTablero(tablero, fila, columna):
    if tablero[fila][columna] == " " or tablero[fila][columna] == "0":
        tablero[fila][columna] = "0"
    return tablero

def esperarJugada(Client_conn,tablero,minas):
    i=0
    tamanio= len(tablero)*len(tablero)
    #print("tamanio: ",tamanio)
    #print("minas: ",minas)
    #print("Restantes: ",tamanio-minas)
    while 1:
        print("Esperando jugada del cliente...")
        data = Client_conn.recv(buffer_size)
        if i==tamanio-minas:
            Client_conn.sendall("2".encode())
            print("Ganaste")
            break
        print("jugada: ", data.decode())
        jugada = data.decode().split(",")
        try:
            fila = int(jugada[0]) - 1
            columna = string.ascii_lowercase.index(jugada[1])
            if tiro(tablero, fila, columna):
                actualizarTablero(tablero, fila, columna)
                imprimirTablero(tablero)
                Client_conn.sendall("0".encode())
                i+=1
            else:
                Client_conn.sendall("1".encode())
                break
        except:
            print("Error en la jugada")
            break


def main():
    limpiaPantalla()
    cliente, TCPServerSocket = prenderServidor()
    tablero,minas,coordenadas = recibirDificultad(cliente)
    inicio = time.time()
    limpiaPantalla()
    imprimirTablero(tablero)
    esperarJugada(cliente,tablero,minas)
    cliente.sendall(str(coordenadas).encode())
    fin = time.time()
    tiempo_transcurrido = fin - inicio
    print("Tiempo de partida: ",tiempo_transcurrido)
    time.sleep(1)
    cliente.sendall(str(tiempo_transcurrido).encode())
    cerrarConexion(cliente)
    apagarServidor(TCPServerSocket)

main()
