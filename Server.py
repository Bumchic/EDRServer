import socketserver
import socket




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
        clientsocket = serversocket.accept()
        print("client connected from " + clientsocket[1])
        clients.appends(clienthandler(clientsocket=clientsocket))
        

class clienthandler:
    
    def __init__(self, clientsocket: socket):
        self.clientsocket = clientsocket
        clientcount = clientcount + 1
        clients.append(self)
        pass
    



if __name__ == "__main__":
    main()