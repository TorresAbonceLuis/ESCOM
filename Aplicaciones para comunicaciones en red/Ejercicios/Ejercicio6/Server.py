#!/usr/bin/env python3
import socket
import threading

HOST = "127.0.0.1"  # Hostname o  dirección IP del servidor
PORT = 65432  # Puerto del servidor
buffer_size = 1024

def worker(Client_conn, Client_addr):
    print("Direccion Clientee:", Client_addr)#imprimir direccion del cliente
    while True:
        data = Client_conn.recv(buffer_size)
        if not data:
            break
        print("Recibido:", data.decode("utf-8"))
        Client_conn.sendall(data)
    print("Conexión cerrada con:", Client_addr)#cerrar conexion cuando termine de recibir
    Client_conn.close()


num = 1#enumerar los clientes
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPServerSocket:
    TCPServerSocket.bind((HOST, PORT))
    TCPServerSocket.listen()
    print("El servidor TCP está disponible y en espera de solicitudes")

    while True:
        Client_conn, Client_addr = TCPServerSocket.accept()
        client_thread = threading.Thread(target=worker, args=(Client_conn, Client_addr))#crear hilo para cada cliente
        client_thread.start()#iniciar hilo
        print("Cliente: ", num, "conectado.")
        num += 1