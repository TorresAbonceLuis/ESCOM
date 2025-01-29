import socket
import threading
import queue

HOST = "127.0.0.1"  # Dirección IP del servidor
PORT = 65432  # Puerto del servidor
buffer_size = 1024

broadcast_queue = queue.Queue()  # Cola para manejar mensajes de broadcast
clients = []
threads = []

def worker(Client_conn, Client_addr):
    print("Dirección Cliente:", Client_addr)
    try:
        while True:
            data = Client_conn.recv(buffer_size)
            if not data:
                break
            print("Número de hilos:" + str(len(clients)))
            print("Recibido:", data.decode("utf-8"))
            Client_conn.sendall(data)
    except:
        print("Conexión cerrada por el cliente:", Client_addr)
    finally:
        Client_conn.close()  # cerrar conexion
        clients.remove((Client_conn, Client_addr))  # quitar de la lista de clientes
        print("Conexión cerrada con:", Client_addr)
        broadcast_queue.put(f"Cliente {Client_addr} se ha desconectado")
        print("Clientes conectados:", len(clients))
        threads.remove(threading.current_thread())  # quitar de la lista de hilos
        print("Número de hilos:", len(threads))

# Función que envía mensajes de broadcast a todos los clientes conectados
def broadcast_messages():
    while True:
        message = broadcast_queue.get()  # obtener mensaje de la cola
        for client_socket, _ in clients:  # iterar la lista de clientes
            client_socket.sendall(message.encode("utf-8"))  # enviar mensaje
        broadcast_queue.task_done()  # marcar tarea como terminada

broadcast_thread = threading.Thread(target=broadcast_messages)  # hilo para enviar mensajes de broadcast
broadcast_thread.setDaemon(True)  # marcar hilo como daemon
broadcast_thread.start()  # iniciar hilo

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPServerSocket:
    TCPServerSocket.bind((HOST, PORT))
    TCPServerSocket.listen()
    print("El servidor TCP está disponible y en espera de solicitudes")
    i=0
    while i!=3:
        Client_conn, Client_addr = TCPServerSocket.accept()  # aceptar conexion
        clients.append((Client_conn, Client_addr))  # agregar a la lista de clientes
        client_thread = threading.Thread(target=worker, args=(Client_conn, Client_addr))  # hilo para cada cliente
        client_thread.start()  # iniciar hilo
        threads.append(client_thread)
        print("Cliente:", len(clients), "conectado.")
        broadcast_queue.put(f"Cliente {Client_addr} se ha conectado")  # enviar mensaje de broadcast
        i+=1

# Esperar a que todos los hilos terminen
for thread in threads:
    thread.join()

# Esto se ejecutará cuando todos los hilos hayan terminado
print("Todos los hilos han terminado. El servidor está cerrado.")
active_threads = threading.enumerate()  # obtener lista de hilos activos
for thread in active_threads:
    print(f"Hilo: {thread.name}, Daemon: {thread.daemon}")
exit(0)  # salir del programa
