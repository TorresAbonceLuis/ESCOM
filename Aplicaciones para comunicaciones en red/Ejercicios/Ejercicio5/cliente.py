import socket
import selectors
import os

sel = selectors.DefaultSelector()

def iniciarCliente(host, port):
    cliente_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_sock.connect((host, port))
    cliente_sock.setblocking(False)
    sel.register(cliente_sock, selectors.EVENT_READ | selectors.EVENT_WRITE, read_write)

def enviarArchivo(socket):
    with open("Bibla.txt","rb") as archivo:
        tamanio = os.path.getsize("Bibla.txt")
        tamanioStr=str(tamanio)
        socket.sendall(tamanioStr.encode())
        archivo.seek(0)
        print("tamanio:",tamanioStr)
        while True:
            bytes = archivo.read(1024)
            if not bytes:
                break
            socket.sendall(bytes)

def read_write(cliente_sock, mask):
    if mask & selectors.EVENT_READ:
        data = cliente_sock.recv(1024)
        if data:
            print('Recibido:', repr(data.decode()))
        else:
            print('Cerrando conexión')
            sel.unregister(cliente_sock)
            cliente_sock.close()
    if mask & selectors.EVENT_WRITE:
        print("Enviando el archivo")
        enviarArchivo(cliente_sock)
        print("Archivo enviado")


server_host = 'localhost'
server_port = 12345

iniciarCliente(server_host, server_port)

print("Esperando evento...")
events = sel.select()
for key, mask in events:
    callback = key.data
    callback(key.fileobj, mask)
