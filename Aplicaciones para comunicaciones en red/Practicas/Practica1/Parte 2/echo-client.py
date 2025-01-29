import socket

HOST = "127.0.0.1"  # El hostname o IP del servidor
PORT = 54321  # El puerto usado por el servidor
msgFromClient = input("Introduce el mensaje a enviar: ")
bytesToSend = str.encode(msgFromClient)
msgFromClient2 = ""
bytesToSend2= str.encode(msgFromClient2)
serverAddressPort = ("127.0.0.1", 54321)
bufferSize = 1024

# Crea un socket UDP del lado del cliente
with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as UDPClientSocket:
    # Enviando mensaje al servidor usando el socket UDP
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    print("Message from Server {}".format(msgFromServer[0]))
    UDPClientSocket.sendto(bytesToSend2, serverAddressPort)
