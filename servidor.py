import socket

def cria_matriz(lst, n):  
    for i in range(0, len(lst), n): 
        yield lst[i:i + n] 

def StrToInt(txt):
    stlist = txt.split(',')
    lista = list(map(int, stlist))
    return lista

def prodMatrix(matrizA, matrizB):
    """Multiplica duas matrizes."""
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
    return matrizR

host = 'localhost'
port = 8001
addr = ((host,port))
serv_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#ban = Banco()
serv_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
serv_socket.bind(addr)
serv_socket.listen(10)

print("aguardando conexão...")

con, cliente = serv_socket.accept()
print("conectado")
print("aguardando mensagem...")
running = True
while(running):
    recebe = con.recv(1024)
    print('mensagem recebida: '+ recebe.decode())
    msg = recebe.decode().split('/')
    if recebe.decode() == 'sair':
        running = False
    elif recebe.decode() == None:
        con.send('erro'.encode())
    
    else:
        n1 = int(msg[0])
        n2 = int(msg[1])
        list1 = StrToInt(msg[2])
        list2 = StrToInt(msg[3])
        matriz1 = list(cria_matriz(list1, n1))
        matriz2 = list(cria_matriz(list2, n2))
        con.send('Produto das Matrizes: {}\n'.format(prodMatrix(matriz1,matriz2)).encode())
        #con.send('Matrizes: {}\n{}\n'.format(matriz1,matriz2).encode())

serv_socket.close()