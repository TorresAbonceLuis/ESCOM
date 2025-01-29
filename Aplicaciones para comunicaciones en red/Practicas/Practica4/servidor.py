import socket
import os

# Configuración del servidor
host = '127.0.0.1'
port = 12345

# Credenciales de usuario y contraseña (puedes almacenar estas en una base de datos)
usuarios = {'usuario1': 'contrasena1', 'usuario2': 'contraseña2'}

# Crear un socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincular el socket al host y al puerto
server_socket.bind((host, port))

# Escuchar conexiones entrantes
server_socket.listen()

print(f"Servidor escuchando en {host}:{port}")

# Aceptar la conexión entrante
client_socket, client_address = server_socket.accept()
print(f"Conexión aceptada desde {client_address}")

# Función para autenticar al usuario
def autenticar_usuario(usuario, contraseña):
    return usuarios.get(usuario) == contraseña

while True:
    # Recibir datos del cliente
    data = client_socket.recv(1024)

    # Si no hay datos, la conexión se cerró
    if not data:
        break

    # Decodificar y mostrar el mensaje recibido
    message = data.decode('utf-8')
    
    # Verificar si el mensaje es un intento de inicio de sesión
    if message.startswith("login:"):
        _, usuario, contraseña = message.split(':')
        if autenticar_usuario(usuario, contraseña):
            respuesta = "Autenticación exitosa"
        else:
            respuesta = "Autenticación fallida"
    else:
        if message.lower() == "dir":
            # Obtener la lista de archivos en el directorio actual
            lista_archivos = "\n".join(os.listdir())

            # Enviar la lista de archivos al cliente
            respuesta = f"Archivos en la ruta actual:\n{lista_archivos}"
        elif message.lower() == "exit":
            # Salir del bucle si el usuario envía 'exit'
            break
        else:
            respuesta = "Comando no reconocido. Introduce otro comando válido."

    # Enviar la respuesta al cliente
    client_socket.sendall(respuesta.encode('utf-8'))
print("Conexión cerrada")
# Cerrar la conexión
client_socket.close()
server_socket.close()
