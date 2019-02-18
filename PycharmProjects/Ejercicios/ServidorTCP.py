import socket

mi_socket = socket.socket()# creamos un objeto
mi_socket.bind(('127.0.0.1', 56505)) #cramos la conección (host,puerto de entrada)
mi_socket.listen(5) #conecciones en cola

while True:
    conexion , addr = mi_socket.accept()
    print('Nueva conexión establecida')
    print(addr)

    conexion.send("Hola desde el servidor")
    conexion.close()
