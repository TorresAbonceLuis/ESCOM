import socket

HOST = "127.0.0.1"  # Dirección de la interfaz de loopback estándar (localhost)
PORT = 65432  # Puerto que usa el cliente (los puertos sin privilegios son > 1023)
buffer_size = 1024

def desconexion(cliente):
    cliente.close()
    print("Cliente desconectado")
clientes = []#lista de clientes

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPServerSocket:
    TCPServerSocket.bind((HOST, PORT))
    while True:
        TCPServerSocket.listen()
        print("El servidor TCP está disponible y en espera de solicitudes")
        conn, addr = TCPServerSocket.accept()#acepta la conexión
        clientes.append((conn, addr))#agregar al cliente a la lista
        for i, (cliente_conn, cliente_addr) in enumerate(clientes):#imprime los clientes
            print(f"Cliente {i + 1}: {cliente_addr}")
        opcion = input("Elija una opción:\n1. Desconectar cliente\n2. Continuar servidor\n3. Cerrar servidor\n")
        if opcion=="1":
            desconectar = input("Cliente a desconectar (0 cancelar): ")
            if desconectar == "0":
                print("cancelado")
            else:
                try:
                    num_cliente = int(desconectar)-1
                    if 0 <= num_cliente < len(clientes):
                        desconexion(clientes[num_cliente][0])
                        del clientes[num_cliente]#borrar al cliente
                    else:
                        print("Número de cliente no válido.")
                except:
                    print("Ingresa un número válido.")
        elif opcion == "2":
            print("Manteniendo el servidor activo")
        elif opcion == "3":#ya que se usa with cierra solo todas las conexiones
            break
        else:
            print("Opción no válida. Por favor, elija 1, 2 o 3.")

