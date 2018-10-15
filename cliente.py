


import socket # importo o modulo de soket


host = "192.168.18.1"
port = 9999

socket1= socket.socket()
socket1.connect((host,port))


oracion = str(input("ingresa una oracion.    "))

socket1.send(oracion) 
numero=socket1.recv(1024) 

print ("la oracion ", oracion, "tiene caracteres: ", numero)
timepo = str(input ("presione enter para terminar..." ))

socket1.close() 
