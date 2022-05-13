import socket
from threading import Thread
matrFim = []
def cria_matriz(lst, n):  
    for i in range(0, len(lst), n): 
        yield lst[i:i + n] 

def StrToInt(txt):
    stlist = txt.split(',')
    lista = list(map(int, stlist))
    return lista

def prodMatrix(matrizA, matrizB):
    """Multiplica duas matrizes."""
    global matrFim
    sizeLA = len(matrizA)
    sizeCA = len(matrizA[0]) # deve ser igual a sizeLB para ser possível multiplicar as matrizes
    sizeCB = len(matrizB[0])
    matrizR = []
    # Multiplica
    for i in range(sizeLA):
        matrizR.append([])
        for j in range(sizeCB):
            val = 0
            for k in range(sizeCA):
                    val += matrizA[i][k]*matrizB[k][j]
            matrizR[i].append(val)
    #return matrizR
    matrFim = matrizR

localIP     = "127.0.0.1"

localPort   = 20001

bufferSize  = 1024

 

# Create a datagram socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 

# Bind to address and ip

UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")

 

# Listen for incoming datagrams

while(True):

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    mesgRecebe = bytesAddressPair[0]

    address = bytesAddressPair[1]

    clientMsg = "Message from Client:{}".format(mesgRecebe)
    clientIP  = "Client IP Address:{}".format(address)
    
    print(clientMsg)
    print(clientIP)
    if mesgRecebe == None:
        msgFromServer       = "erro!"
        bytesToSend         = str.encode(msgFromServer)
        # Sending a reply to client
        UDPServerSocket.sendto(bytesToSend, address)
    elif mesgRecebe =='sair':
        msgFromServer       = "tchau!"
        bytesToSend         = str.encode(msgFromServer)
        # Sending a reply to client
        UDPServerSocket.sendto(bytesToSend, address)
    else:
        msg1 = str(mesgRecebe)
        msg = msg1.split("'")
        #print(msg)
      
        mat = msg[1].split('/')
        n1 = int(mat[0])
        n2 = int(mat[1])
        list1 = StrToInt(mat[2])
        list2 = StrToInt(mat[3])
        matriz1 = list(cria_matriz(list1, n1))
        matriz2 = list(cria_matriz(list2, n2))
        t = Thread(target=prodMatrix(matriz1,matriz2))
        t.start()
        msgFromServer       = 'Produto das Matrizes: {}\n'.format(matrFim)
        bytesToSend         = str.encode(msgFromServer)
        # Sending a reply to client
        UDPServerSocket.sendto(bytesToSend, address)
   