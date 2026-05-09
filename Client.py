import socket
from os import read
import re

Host = None
port = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


while True:
    ip = input('input server ip: ')
    if re.search("^([1-9][0-9]?|1[0-9]{2}|2[01][0-9]|22[0-3])(\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}$", ip):
        break
    print('ip input invalid, try again')
try:
    server.connect((Host, port))
    print('server connection success')
except TimeoutError as e:
    print('server connection failed: ' + e)
except Exception as e:
    print(e)
