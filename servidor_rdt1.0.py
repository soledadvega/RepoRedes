from socket import *

def create_UDPsocket(address, port):
	UDPsocket = socket(AF_INET, SOCK_DGRAM)
	UDPsocket.bind((address, port))
	return UDPsocket
    
def deliver_data(data): #Saca el encabezado y le spasa los datos a la capa de aplicacion, en este caso pasarselo a la pantalla
    print(data)

def extract(pocket): #por ahora extraer los datos del paquete y devolverlo--CRUSIAL!!! audio para completar 
    return pocket.decode('utf-8') #proceso inverso de encode
    
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
        
    close_socket(servidor)
    
    

    
