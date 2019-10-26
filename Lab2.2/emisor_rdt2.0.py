from constantes import *
from socket import *
from paquete import *

def create_socket():
    UDPsocket=socket(AF_INET, SOCK_DGRAM) # creo el socket protocolo de red IP, protocolo transporte UDP
    return UDPsocket


def rdt_send():
    dato=input('ingrese un mensaje:  ')
    return(dato.encode('utf-8'))


def make_pkt(sendpkt):
    pkt=Paquete(EMISOR_PORT , RECEPTOR_PORT, sndpkt, 0)
    cksum=calcular_checksum(pkt)
    pkt.set_checksum(cksum)
    return pkt


def udp_send(socket, mensaje, receiver): #data y reciber
    mensaje=dumps((mensaje, receiver))
    socket.sendto(mensaje, (NETWORK_IP,NETWORK_PORT))#con esto mando a la red

def rdt_recv(socket):
    data=socket.recvfrom(2048)
    receptor, paquete=loads(data)
    return emisor, paquete

def close_socket(socket, signal, frame):
    print ("\n\rCerrando socket")
    socket.close()
    exit(0)


if __name__ == "__main__":

        cliente=create_socket() # Creamos el socket
        signal.signal(signal.SIGINT, partial(close_socket, cliente))#esta funcion toma el socketal final
        while True:
                secuencia=0
                data=rdt_send() # Leemos el mensaje desde teclado
                recv_paquete=rdt_recv(cliente)
                paquete=make_pkt(data) # Hacemos el paquete
                destinatario=(RECEPTOR_IP, RECEPTOR_PORT) # Establecemos el destinatario
                udp_send(cliente,destinatario, paquete) # Enviamos el mensaje
                if rdt_recv() and corrupto(paquete) is Ack(recv_paquete, 1):
                    udt_send(paquete)
                if red_recv() and not corrupto and Ack(recv_paquete, 0):
                    secuencia=(secuencia + 1) // 2




        # si me llega un paquete y esta corrupto envio de nuevo hasta que me llege el ṕositivo
        # else : sumar 1 a la secuencia
        close_socket(cliente)
