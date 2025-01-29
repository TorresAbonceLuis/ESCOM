import socket
import selectors
import time

sel = selectors.DefaultSelector()

def iniciarCliente(host, port):
    cliente_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_sock.connect((host, port))
    cliente_sock.setblocking(False)
    sel.register(cliente_sock, selectors.EVENT_READ | selectors.EVENT_WRITE, read_write)

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
        mensaje="1"
        while 1:
            print('Enviando:', mensaje)
            cliente_sock.sendall(mensaje.encode())
            time.sleep(1)


server_host = 'localhost'
server_port = 12345

iniciarCliente(server_host, server_port)

while True:
    print("Esperando evento...")
    events = sel.select()
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)
