from constants import *
from socket import *
from pickle import *
from packet import *
from network import *

def create_socket():
	UDPsocket = socket(AF_INET, SOCK_DGRAM)
	UDPsocket.bind((RECEIVER_IP, RECEIVER_PORT)) #es para saber donde tiene que escuchar el ip y puerto del archivo constantes
	return UDPsocket


def deliver_data(mensaje):
	print(mensaje)

def extract(packet):  #etrae el paquete
    data=packet.get_data()
    return data

def rdt_recv(socket):
	data=socket.recv(2048)
	paquete=loads(data) #load descomprime
	return paquete

def close_socket(socket, signal, frame):
	print ("\n\rCerrando socket")
	socket.close()
	exit(0)

if __name__ == "__main__":
	servidor=create_socket()  # creamos socket receiver

	signal.signal(signal.SIGINT, partial(close_socket, servidor)) #registra la senial de salida
	print("Listo para recibir mensajes...") #Imprimimos el mensaje
    # Itera indefinidamente
	while True:
		packet=rdt_recv(servidor) #recibe de la red un paquete
		print(packet)
		data=extract(packet) #extrae los datos
		print("dos")
		deliver_data(data) #entrega datos a la capa de aplicacion

	close_socket(servidor)
