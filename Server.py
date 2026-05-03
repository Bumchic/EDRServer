import socketserver
import socket


class clienthandler:
    
    def __init__(self, clientsocket: socket):
        self.clientsocket = clientsocket
        global clientcount
        clientcount = clientcount + 1
        clients.append(self)
        pass
    


ip:str = "127.0.0.1"
port:int = 8080
clientcount:int = 0
clients: list[clienthandler] = []

def main():
    print('running')
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind((ip, port))
    serversocket.listen()



    while True:
        clientsocket, addr = serversocket.accept()
        print("client connected from ", addr)
        clients.append(clienthandler(clientsocket=clientsocket))
        





if __name__ == "__main__":
    main()