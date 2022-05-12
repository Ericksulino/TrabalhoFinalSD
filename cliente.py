import socket
ip = 'localhost'
port = 8001
addr = ((ip,port))
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(addr)

mensagem = ''

while(mensagem != 'sair'):
    mensagem = input('Digite uma mensagem para enviar ao servidor:')
    client_socket.send(mensagem.encode())
    #print('Mensagem enviada!')
    print('Mensagem recebida:' + client_socket.recv(1024).decode())

print('Saindo...')
client_socket.close()