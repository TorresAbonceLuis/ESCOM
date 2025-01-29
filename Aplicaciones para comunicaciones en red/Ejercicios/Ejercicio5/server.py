#!/usr/bin/env python3
import socket
import selectors

sel = selectors.DefaultSelector()

def accept(sock_a, mask):
    sock_conn, addr = sock_a.accept()  # Should be ready
    print('aceptado', sock_conn, ' de', addr)
    sock_conn.setblocking(False)
    sel.register(sock_conn, selectors.EVENT_READ | selectors.EVENT_WRITE, read_write)

def recibirArchivo(sock_conn, tamanio):
    tamanioInt = int(tamanio)
    print(tamanio)
    with open("ArchivoCopiado.txt", "wb") as archivo:
        while tamanioInt > 0:
            try:
                data = sock_conn.recv(1024)  # Recibe hasta 1024 bytes a la vez
                if not data:
                    break
                archivo.write(data)
                tamanioInt -= len(data)
            except:
                pass


def read_write(sock_c, mask):
    if mask & selectors.EVENT_READ:
        try:
            tamanio = sock_c.recv(1024)
            print(tamanio)
            if tamanio:
                tamanioInt = int(tamanio)
                recibirArchivo(sock_c, tamanioInt)
                print('respondiendo', repr(tamanio), 'a', sock_c)
                sock_c.sendall("Recibido".encode())  # Hope it won't block
            else:
                print('cerrando', sock_c)
                sel.unregister(sock_c)
                sock_c.close()
        except:
            pass

with socket.socket() as sock_accept:
    sock_accept.bind(('localhost', 12345))
    sock_accept.listen(100)
    sock_accept.setblocking(False)
    sel.register(sock_accept, selectors.EVENT_READ, accept)
    while True:
        print("Esperando evento...")
        events = sel.select()
        for key, mask in events:
            callback = key.data
            callback(key.fileobj, mask)
