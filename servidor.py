import socket

def cria_matriz(lst, n):  
    for i in range(0, len(lst), n): 
        yield lst[i:i + n] 

def StrToInt(txt):
    stlist = txt.split(',')
    lista = list(map(int, stlist))
    return lista

def getLinha(matriz, n):
    return [i for i in matriz[n]]  

def getColuna(matriz, n):
    return [i[n] for i in matriz]


def multiMatriz(mat1,mat2):
    mat1lin = len(mat1)                               
    mat2col = len(mat1[0])            
    matRes = []                        
    for i in range(mat1lin):           
        matRes.append([])

        for j in range(mat2col):
            # multiplica cada linha de mat1 por cada coluna de mat2;
            listMult = [x*y for x, y in zip(getLinha(mat1, i), getColuna(mat2, j))]

            # e em seguida adiciona a matRes a soma das multiplicações
            matRes[i].append(sum(listMult))

    return(matRes)

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
        con.send('Produto das Matrizes: {}\n'.format(multiMatriz(matriz1,matriz2)).encode())
        #con.send('Matrizes: {}\n{}\n'.format(matriz1,matriz2).encode())

serv_socket.close()