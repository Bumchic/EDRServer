import socket

ip = "127.0.0.1"
port = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if(server.connect((ip, port))):
    print('server connection success')

