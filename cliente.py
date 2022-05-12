import socket
ip = 'localhost'
port = 8001
addr = ((ip,port))
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(addr)



msg = input("Digite a msg: ")
client_socket.send(msg)
#extr = client_socket.recv(1024).decode()