import threading
import socket
import queue

def handle_client(client_socket, message_queue):
    while True:
        data = client_socket.recv(1024)  # Recibe datos del cliente
        if not data:
            break  # Si no hay datos, la conexión se ha cerrado
        message = data.decode()
        print(f"Recibido: {message}")
        message_queue.put(message)  # Coloca el mensaje en la cola para que el hilo principal lo reciba

    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 8888))
    server_socket.listen(5)

    print("Servidor esperando conexiones en el puerto 8888...")

    message_queue = queue.Queue()  # Crea una cola para manejar mensajes desde los hilos secundarios

    while True:
        client_socket, addr = server_socket.accept()  # Acepta conexiones de clientes
        print(f"Conexión establecida con {addr}")
        
        client_handler = threading.Thread(target=handle_client, args=(client_socket, message_queue))
        client_handler.start()  # Inicia un nuevo hilo para manejar al cliente

        # En el hilo principal, verifica la cola para ver si hay mensajes recibidos
        while not message_queue.empty():
            received_message = message_queue.get()
            print(f"Mensaje recibido en el hilo principal: {received_message}")

if __name__ == "__main__":
    main()
