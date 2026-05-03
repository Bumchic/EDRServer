import socketserver
import socket


class clienthandler:
    
    def __init__(self, clientsocket: socket):
        self.clientsocket = clientsocket
        global clientcount
        clientcount = clientcount + 1
        clients.append(self)
        pass
    


Host = None
port:int = 8080
clientcount:int = 0
clients: list[clienthandler] = []

def main():
    print('running')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((Host, port))
        s.listen(1)
        while True:
            clientsocket, addr = s.accept()
            with clientsocket:
                print("client connected from ", addr)
                clients.append(clienthandler(clientsocket=clientsocket))










if __name__ == "__main__":
    main()