from constants import *
from socket import *
from pickle import *
from packet import *

def create_UDPsocket():
	UDPsocket=socket(AF_INET, SOCK_DGRAM) # creo el socket protocolo de red IP, protocolo transporte UDP
	return UDPsocket

def rdt_send():
    data=input('ingrese un mensaje:  ')
    return(data.encode('utf-8'))

def make_pkt(data):
    pkt=Packet(SENDER_PORT, RECEIVER_PORT, data)
    return pkt

def udp_send(socket, receiver, packet):
	datos=dumps((receiver,packet))
	socket.sendto(datos,(NETWORK_IP, NETWORK_PORT))#con esto mando a la red
 # uso la direccion de la red y tengo q usar la del emisor

def close_socket(socket, signal, frame):
	print ("\n\rCerrando socket")
	socket.close()
	exit(0)

if __name__ == "__main__":
	cliente=create_UDPsocket() # Creamos el socket

    #Registramos la senial
	signal.signal(signal.SIGINT, partial(close_socket, cliente))#esta funcion toma el socket al final
    #Iteramos indefinidamente
	while True:
		data=rdt_send() # Leemos el mensaje desde teclado
		pkt=make_pkt(data) #crea el paquete
		receiver=(RECEIVER_IP, RECEIVER_PORT) # Establecemos el destinatario
		udp_send(cliente, receiver, pkt) # Enviamos el mensaje
	close_socket(cliente)
