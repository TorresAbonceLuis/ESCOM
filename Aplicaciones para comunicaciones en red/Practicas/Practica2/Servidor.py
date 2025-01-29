import socket
import random
import os
import string
import time
import threading
import pickle
from threading import Barrier
import queue
import sys

HOST = "192.168.68.108"
PORT = 65432
buffer_size = 1024

hilos = []
conexiones = []
numero_clientes_esperados = 2
clientes_conectados = 0
mensaje_queue = queue.Queue()
coordenadasTiros = []

def prenderServidor():
    TCPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPServerSocket.bind((HOST, PORT))
    TCPServerSocket.listen()
    print("El servidor está disponible")
    return TCPServerSocket

def jugar(serialized_data,Client_conn):
    inicio = time.time()
    datos_deserializados = pickle.loads(serialized_data)
    tablero, minas, coordenadas = datos_deserializados["tablero"], datos_deserializados["minas"], datos_deserializados["coordenadas"]
    esperarJugada(Client_conn, tablero, minas)
    enviarBroadcast(coordenadas)  # Enviar coordenadas de las minas
    fin = time.time()
    tiempo_transcurrido = fin - inicio
    print("Tiempo de partida: ", tiempo_transcurrido)
    time.sleep(1)
    Client_conn.sendall(str(tiempo_transcurrido).encode())
'''
def worker(Client_conn, Client_addr,barrera,serialized_data):
    barrera.wait()#esperar a que se conecten todos los clientes
    print("direccion del cliente", Client_addr)
    #print(threading.current_thread().name, 'esperando en la barrera con {} hilos mas'.format(barrera.n_waiting))
    #worker_id=barrera.wait()
    #print(threading.current_thread().name,'despues de la barrera',worker_id)
    datos_deserializados = pickle.loads(serialized_data)
    tablero, coordenadas, minas = datos_deserializados ["tablero"] , datos_deserializados["coordenadas"], datos_deserializados["minas"]
    time.sleep(1)
    esperarJugada(Client_conn,tablero,minas)
    print("Conexion cerrada")
    Client_conn.shutdown(socket.SHUT_WR)
    Client_conn.close()
    print("Terminado")
'''

def worker(TCPClientSocket,barrera):
    barrera.wait()#esperar a que se conecten todos los clientes
    try:
        while True:
            data = TCPClientSocket.recv(buffer_size).decode()
            if not data:
                break
            mensaje_queue.put(data)
    except:
        pass

def enviarBroadcast(mensaje):
    global hilos
    i = 0
    for client_socket in hilos:
        try:
            client_socket.sendall(mensaje.encode())
            print(i)
            i += 1
        except Exception as e:
            print(f"Error al enviar mensaje de broadcast: {e}")
            # Eliminar el hilo del cliente que ha tenido un error de conexión
            hilos.remove(client_socket)
            client_socket.close()  # Cerrar el socket del cliente que se desconectó
            desconectarClientes()  # Puedes invocar esta función aquí para notificar a los demás clientes si es necesario

def desconectarClientes():
    global hilos
    enviarBroadcast("desconexion")
    for client_socket in hilos:
        client_socket.close()
    hilos = []  # Limpiar la lista de hilos después de desconectar a todos los clientes
    limpiaPantalla()
    print("Conexiones cerradas")
    sys.exit()

def esperarCliente(TCPServerSocket, serialized_data):
    global clientes_conectados
    barrera = threading.Barrier(numero_clientes_esperados)
    while numero_clientes_esperados != clientes_conectados:
        Client_conn, Client_addr = TCPServerSocket.accept()
        print("Se conectó un cliente")
        t = threading.Thread(target=worker, args=(Client_conn,barrera))
        t.start()
        clientes_conectados += 1
        hilos.append(Client_conn)  # Agregar el socket del cliente a la lista de hilos
        conexiones.append(Client_conn)
    enviarBroadcast("El juego ha comenzado.")  # Enviar mensaje de inicio a todos los clientes
    print("Se envio el mensaje de bienvenida")
    datos_deserializados = pickle.loads(serialized_data)
    dificultad = datos_deserializados["dificultad"]
    print(str(dificultad))
    time.sleep(1)
    enviarBroadcast(str(dificultad)) # 1 principiante #2 avanzado
    tablero, coordenadas, minas = datos_deserializados ["tablero"] , datos_deserializados["coordenadas"], datos_deserializados["minas"]
    time.sleep(1)
    imprimirTablero(tablero)
    resultado = esperarJugada(Client_conn,tablero,coordenadas, minas)
    limpiaPantalla()
    print("El juego ha terminado")
    print("Cerrando conexiones...")
    time.sleep(1)
    enviarBroadcast("fin")
    time.sleep(1)
    enviarBroadcast(str(coordenadas))
    time.sleep(1)
    for i in range(numero_clientes_esperados-1):
        print (i)
        data = mensaje_queue.get()
    for Client_conn in conexiones:
        Client_conn.shutdown(socket.SHUT_WR)
        Client_conn.close()
    print("conexion cerrada")

    
def apagarServidor(TCPServerSocket):
    TCPServerSocket.close()
    
def cerrarConexion(Client_conn):
    Client_conn.close()

def recibirDificultad():
    dificultad = random.choice(["1", "2"])  # Elige aleatoriamente entre 1 (Principiante) y 2 (Avanzado)
    print("El servidor eligió la dificultad:", dificultad)
    if dificultad == "1":  # Principiante
        minas = 10
        print("Principiante")
        tableros, coordenadas = tablero(9, 9, minas)
        return tableros, minas, coordenadas, dificultad
    elif dificultad == "2":  # Avanzado
        minas = 40
        print("Avanzado")
        tableros, coordenadas = tablero(16, 16, minas)
        return tableros, minas, coordenadas, dificultad

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
        return 0#Perdió
    elif tablero[fila][columna] == "0":
        return 1# misma casilla
    else:
        return 2#sigue jugando

def actualizarTablero(tablero, fila, columna):
    limpiaPantalla()
    if tablero[fila][columna] == " " or tablero[fila][columna] == "0":
        tablero[fila][columna] = "0"
    return tablero

def esperarJugada(Client_conn,tablero,coordenadas, minas):
    i=0
    tamanio= len(tablero)*len(tablero)
    while 1:
        print("Esperando jugada del cliente...")
        data = mensaje_queue.get()#Esperar a que el cliente envíe una jugada
        if i==tamanio-minas:#Ganó
        #if i == 1:
            enviarBroadcast("3")
            print("Ganaste")
            mensaje = str(fila) +","+ str(columna) +","+ "3"
            enviarBroadcast(mensaje)
            break
        jugada = data.split(",")
        try:
            fila = int(jugada[0]) - 1
            columna = string.ascii_lowercase.index(jugada[1])
            resultado= tiro(tablero, fila, columna)
            coordenadasTiros.append((fila,columna,resultado))
            if resultado == 0:#Perdió
                print("Perdiste")
                actualizarTablero(tablero, fila, columna)
                imprimirTablero(tablero)
                enviarBroadcast("0")
                i+=1
                mensaje = str(fila) +","+ str(columna) +","+ "0"
                print(mensaje)
                time.sleep(1)
                enviarBroadcast(mensaje)
                break
            elif resultado == 1:#misma casilla
                enviarBroadcast("1")
                mensaje = str(fila) +","+ str(columna) +","+ "1"
                enviarBroadcast(mensaje)
            else:#sigue jugando
                actualizarTablero(tablero, fila, columna)
                imprimirTablero(tablero)
                enviarBroadcast("2")
                enviarBroadcast(str(coordenadasTiros))
                i+=1
        except:
            print("Error en la jugada")
            break
    enviarBroadcast(str(coordenadas))
    return resultado

def main():
    global clientes_conectados  # Declarar clientes_conectados como global en la función main
    TCPServerSocket = prenderServidor()
    tablero, minas, coordenadas, dificultad = recibirDificultad()  # Elegir dificultad antes de esperar a los clientes
    data_dict = {
        "tablero": tablero,
        "minas": minas,
        "coordenadas": coordenadas,
        "dificultad" : dificultad
    }
    serialized_data = pickle.dumps(data_dict)#Serializar el diccionario
    print(f"Esperando {numero_clientes_esperados} clientes...")
    try:
        esperarCliente(TCPServerSocket,serialized_data)
    except KeyboardInterrupt:
        print("Apagando el servidor...")
        apagarServidor(TCPServerSocket)
main()
