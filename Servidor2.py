import socket

miSocket= socket.socket()
#Ahora podríamos hacer:
#miSocket.bind(('localhost', 8000))
#Pero en este caso haremos:
miSocket.bind(('', 1234))
miSocket.listen(5)

while True:

    conexion, addr = miSocket.accept()
    print("Conexion establecida de ", addr)

    peticion= conexion.recv(1024).decode()
    print(peticion)

    if peticion == "hola":
        conexion.send("Adios".encode())
    elif peticion == "adios":
        conexion.send("Servidor cerrado".encode())
        break
    conexion.send(b'Hola, soy el servidor')
    conexion.close()

