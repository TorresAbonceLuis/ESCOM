import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 8888))  # Conéctate al servidor en el puerto 8888

    while True:
        message = input("Ingrese un mensaje para enviar al servidor: ")
        client_socket.sendall(message.encode())  # Envía el mensaje al servidor

        if message.lower() == "exit":
            break  # Si el mensaje es "exit", cierra la conexión y termina el programa

    client_socket.close()  # Cierra el socket al finalizar

if __name__ == "__main__":
    main()
