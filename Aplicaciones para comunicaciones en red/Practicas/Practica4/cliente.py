import socket

# Configuración del cliente
host = '127.0.0.1'
port = 12345

# Crear un socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar al servidor
client_socket.connect((host, port))

# Función para ingresar credenciales de usuario
def ingresar_credenciales():
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")
    return f"login:{usuario}:{contraseña}"

# Autenticación del usuario
while True:
    mensaje_autenticacion = ingresar_credenciales()
    client_socket.sendall(mensaje_autenticacion.encode('utf-8'))

    # Recibir respuesta del servidor
    respuesta = client_socket.recv(1024)
    print(respuesta.decode('utf-8'))

    # Salir del bucle si la autenticación es exitosa
    if respuesta.decode('utf-8') == "Autenticación exitosa":
        break

# Envío de mensajes después de la autenticación
while True:
    # Solicitar al usuario que ingrese un mensaje
    message = input("Ingrese un comando (o 'exit' para salir): ")

    # Enviar el mensaje al servidor
    client_socket.sendall(message.encode('utf-8'))

    # Recibir y mostrar la respuesta del servidor
    respuesta = client_socket.recv(1024)
    print(respuesta.decode('utf-8'))

    # Salir si el usuario ingresa 'exit'
    if message.lower() == 'exit':
        break

# Cerrar la conexión
client_socket.close()
