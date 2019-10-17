from socket import *
from pickle import *
from paquete import *
from constantes import *

def create_UDPsocket(IP, PORT): #crea un socket con las direcciones como parametros
	UDPsocket = socket(AF_INET, SOCK_DGRAM)
	UDPsocket.bind((IP, PORT))
	return UDPsocket


def deliver_data(data):   #recibe los datos e imprime por pantalla
    print(data)

def extract(pocket):    #extrae los datos del paquete y los devuelve
    data=pocket.get_data()
    return data

def close_socket(socket):  #cierra el socket creado
    socket.close()

def rdt_recv(socket): #recive un paquete a traves de un socket 
    dato=socket.recv(2048)   #usa la lib. pickle
    paquete=loads(dato)  #toma como argum datos recv. del socket
    return paquete  #y vuelve a conv. en paquete

if __name__ == "__main__":
    servidor=create_UDPsocket(RECEIVER_IP, RECEIVER_PORT)
    print('Servidor corriendo')
    while 1:
        packet=rdt_recv(servidor)
        data=extract(packet)
        deliver_data(data)

    close_socket(servidor)
