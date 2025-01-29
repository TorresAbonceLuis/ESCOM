import socket
import selectors

sel = selectors.DefaultSelector()

def accept(sock_a, mask):
    sock_conn, addr = sock_a.accept()  # Should be ready
    print('Aceptado', sock_conn, 'de', addr)
    sock_conn.setblocking(False)
    sel.register(sock_conn, selectors.EVENT_READ, read_write)

def read_write(sock_c, mask):
    if mask & selectors.EVENT_READ:
        data = sock_c.recv(1024)  # Should be ready
        if data:
            print('Recibido', repr(data), 'de', sock_c)
        else:
            print('Cerrando', sock_c)
            sel.unregister(sock_c)
            sock_c.close()

server_host = 'localhost'
server_port = 12345

with socket.socket() as sock_accept:
    sock_accept.bind((server_host, server_port))
    sock_accept.listen(100)
    sock_accept.setblocking(False)
    sel.register(sock_accept, selectors.EVENT_READ, accept)

    while True:
        print("Esperando evento...")
        events = sel.select()
        for key, mask in events:
            callback = key.data
            callback(key.fileobj, mask)

