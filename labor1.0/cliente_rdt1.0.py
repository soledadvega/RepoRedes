from socket import *
from network import *

def create_UDPsock():
	UDPsocket = socket(AF_INET, SOCK_DGRAM)
	return UDPsocket

def rdt_send(): #de la capa de aplicacion a la capa de transpórte
    data=input('ingrese un mensaje:  ') #lee desde teclado
    return data.encode('utf-8')  #el encode lo codifica mueve datos codificados

def make_pkt(data):#mandar tal cual lo recibe, crea el paquete
    pkt=Packet(SENDER_IP, RECEIVER_PORT, data)
    return pkt

def udp_send(socket, receiver, data):  #si me toma el socket y los datos y hace send en los datos
    dato=dumps(dato,(receiver, Packet))
    socket.sendto(datO, (NETWORK_IṔ, NETWORK_PORT))

def close_socket(socket):
    socket.close()

if __name__ == "__main__":
    cliente=create_UDPsock()
    while 1: #ciclo eterno
        data=rdt_send()
        paquete=make_pkt(data)
        udp_send(cliente,paquete)
    close_socket(cliente)
