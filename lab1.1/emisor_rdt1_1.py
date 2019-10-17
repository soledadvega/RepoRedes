from socket import *
from pickle import *
from paquete import *
from constantes import *

def create_UDPsock(IP, PORT):  #crea un socket con dir provis x la capa de transp
	UDPsocket=socket(AF_INET, SOCK_DGRAM)
	return UDPsocket

def rdt_send():   #de la capa de aplicacion a la capa de transpórte
    data=input('ingrese un mensaje:  ')   #ingresar msj por teclado
    return(data.encode('utf-8'))   #encode codifica, mueve datos codificados

def make_pkt(data):  #crea el paquete, manda tal cual lo recibe
    pkt=Packet(SOURCE_PORT, RECEIVER_PORT, data)
    return pkt

def udp_send(socket, pkt):   #toma el socket y los datos y hace send en los datos
    data=dumps(pkt)    #genera los datos que envia a traves del socket, a partir de un paquete
    socket.sendto(data, (RECEIVER_IP, RECEIVER_PORT))

def close_socket(socket):    #cierra el socket 
    socket.close()

if __name__ == "__main__":
    cliente=create_UDPsock(RECEIVER_IP, RECEIVER_PORT)#
    while 1:     #ciclo eterno
        data=rdt_send()
        pkt=make_pkt(data)
        udp_send(cliente, pkt)

    close_socket(cliente)
