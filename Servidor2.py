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

    conexion.send(b'Hola, soy el servidor')
    conexion.close()

