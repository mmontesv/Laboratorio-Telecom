import socket

mi_socket = socket.socket()
mi_socket.connect(('127.0.0.1', 56505))

mi_socket.send("Hola desde el cliente")
respuesta = mi_socket.recv(1024) #respuesta desde el buffer (1024 bytes)

print(respuesta)
print('Hola Mundo')
mi_socket.close()