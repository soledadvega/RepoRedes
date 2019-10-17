from socket import *

def create_UDPsocket(address, port): # crea un socket con las direcciones provistas como parametros
	UDPsocket = socket(AF_INET, SOCK_DGRAM) #permite recibir un paquete a través de un socket UDP
	UDPsocket.bind((address, port))
	return UDPsocket

def deliver_data(data): #Saca el encabezado y le pasa los datos a la capa de aplicacion
    print(data)         # en este caso imprimir por pantalla

def extract(packet): #por ahora extraer los datos del paquete y devolverlo
    return packet.decode('utf-8') #proceso inverso de encode

def rdt_rcv (socket):#de mi socket recibo el paquete y lo devuelve
    packet=socket.recv(2048)
    return packet

def close_socket(socket):
    socket.close()

if __name__ == "__main__":
    servidor=create_UDPsocket('localhost',20000)
    print('Servidor corriendo')
    while 1:
        paquete=rdt_rcv(servidor)
        data=extract(paquete)
        deliver_data(data)

    close_socket(servidor)    #cierra el socket creado
