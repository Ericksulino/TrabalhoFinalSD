import socket

#mensagem = '2/3/2,3,4,6/1,3,0,2,1,1'
mensagem = ''
#for i in range(1):
while(mensagem != 'sair'):
    mensagem = input('Digite uma mensagem para enviar ao servidor:')

    #msgFromClient       = "Hello UDP Server"

    bytesToSend         = str.encode(mensagem)

    serverAddressPort   = ("127.0.0.1", 20001)

    bufferSize          = 1024

    

    # Create a UDP socket at client side

    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    

    # Send to server using created UDP socket

    UDPClientSocket.sendto(bytesToSend, serverAddressPort)

    

    msgFromServer = UDPClientSocket.recvfrom(bufferSize)

    

    msg = "Message from Server {}".format(msgFromServer[0])

    print(msg)