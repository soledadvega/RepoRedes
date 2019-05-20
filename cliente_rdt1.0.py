from socket import *

def create_UDPsock():
	UDPsocket = socket(AF_INET, SOCK_DGRAM)
	return UDPsocket	
    
def rdt_send(): #de la capa de aplicacion a la capa de transpórte
    data=input('ingrese un mensaje:  ') #lee desdde teclado
    return(data.encode('utf-8'))#el encode lo codifica mueve datos codificados 
    
def make_pkt(data):#voy a mandar tal cual lo recibe, crea el paquete 
    return data   
    
def udp_send(socket, data):#si me toma el socket y los datos y hace send en los datos 
    socket.sendto(data, ('localhost',20000))
    
def close_socket(socket):
    socket.close()
    
if __name__ == "__main__":
    cliente=create_UDPsock()
    while 1: #ciclo eterno 
        data=rdt_send()
        paquete=make_pkt(data)
        udp_send(cliente,paquete)
    close_socket(cliente)    
    

