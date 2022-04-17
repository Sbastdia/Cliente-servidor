import socket

miSocket= socket.socket()
miSocket.connect(('', 1234))

miSocket.send(b'Hola, soy el cliente')
respuesta = miSocket.recv(1024)

print (respuesta)
miSocket.close()

